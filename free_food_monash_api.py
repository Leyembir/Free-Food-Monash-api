import subprocess
import time
from fastapi import FastAPI, HTTPException, File, UploadFile, Depends, Body
from fastapi.responses import JSONResponse, 
import jwt
from security import SECRET_KEY, ALGORITHM
from free_food_monash import creating_json_object
from mangum import Mangum
from security import get_password_hash, verify_password, generate_token_for_user
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jwt import PyJWTError

PATH_TO_IMAGE = r'C:\Users\amir0\Documents\Python project amir\\images'


credentials_exception = HTTPException(
    status_code=401, 
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

app = FastAPI()

process = None

def start_server():
    global process
    if process:
        process.terminate()
        process.wait()
    process = subprocess.Popen(["uvicorn", "free_food_monash_api:app", "--reload"])



class LoginRequest(BaseModel):
    username: str
    password: str

class TokenData(BaseModel):
    username: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:19006"],  # Allow only this origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Helper function to split time ranges into separate start and end times
handler = Mangum(app)


# Hardcoded user credentials
HARDCODED_USERNAME = "test"
HARDCODED_PASSWORD_HASH = get_password_hash("test")

security = HTTPBearer()
#Check token:


def check_token(authorization: HTTPAuthorizationCredentials = Depends(security)):
    token = authorization.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except PyJWTError:
        raise HTTPException(status_code=403, detail="Invalid token")
    return token

# Step 3: Create a route handler function
@app.get("/json-object")
def get_json_object():
    
    json_object = creating_json_object()

    # Step 4: Return the JSON object as a response
    return JSONResponse(content=json_object)



@app.post("/upload/photo/")
async def upload_photo(token: str = Depends(check_token), file: UploadFile = File(...)):
    try:
        with open("./images/free_food1.jpg", "wb") as f:
            contents = await file.read()
            f.write(contents)
            start_server()
        return JSONResponse(content={"success": True})
    except Exception as e:
        print("Error saving photo:", e)
        return JSONResponse(content={"success": False})
    # Trigger a restart by modifying a file


    

@app.post("/api/login")
def login(data: LoginRequest):
    if data.username == HARDCODED_USERNAME and verify_password(data.password, HARDCODED_PASSWORD_HASH):
        token = generate_token_for_user(data.username)
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Incorrect username or password")