from pydantic import BaseModel
from security import get_password_hash, verify_password

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

users = []

def get_user_by_username(username: str):
    return next((user for user in users if user.username == username), None)

def create_user(user: UserCreate):
    existing_user = get_user_by_username(user.username)
    if existing_user:
        raise ValueError("User already exists!")
    
    user_dict = user.dict()
    user_dict['id'] = len(users) + 1
    user_dict['password'] = get_password_hash(user_dict['password'])  # Store hashed password
    new_user = User(**user_dict)
    users.append(new_user)
    return new_user

def verify_user_credentials(username: str, password: str):
    user = get_user_by_username(username)
    if not user:
        return False
    return verify_password(password, user.password)

