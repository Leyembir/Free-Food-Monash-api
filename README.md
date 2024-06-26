

# Free Food Monash API

This project provides an API to manage and display free food events at Monash University. The API is built using FastAPI and performs OCR (Optical Character Recognition) to read event details from images and expose these details via endpoints.

## Features

- User authentication and token generation.
- OCR to extract event details from images.
- API endpoints to upload images and retrieve event details.
- CORS support for cross-origin requests.

## Project Structure

```
.
├── free_food_monash.py          # Core OCR and event processing logic
├── free_food_monash_api.py      # FastAPI application with endpoints
├── user.py                      # User management and authentication logic
├── security.py                  # Security functions for password hashing and token generation
├── requirements.txt             # Project dependencies
├── runtime.txt                  # Python runtime version
├── Procfile                     # For deployment purposes
├── Aptfile                      # System-level dependencies
```

## Installation

1. **Clone the repository**

    ```sh
    git clone https://github.com/yourusername/free_food_monash.git
    cd free_food_monash
    ```

2. **Install dependencies**

    Make sure you have Python 3.10.12 installed. Then, install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

3. **Install system-level dependencies**

    Use the `Aptfile` to install system dependencies. For example, if deploying on Heroku, these will be installed automatically. Locally, you might need to install them manually.

4. **Set up the environment**

    Ensure you set the `SECRET_KEY` in `security.py` to a strong, random value.

## Usage

1. **Start the FastAPI server**

    ```sh
    uvicorn free_food_monash_api:app --reload
    ```

2. **API Endpoints**

    - `POST /api/login`: Login and receive a token.
    - `POST /upload/photo/`: Upload a photo to process and extract event details. Requires a valid token.
    - `GET /json-object`: Retrieve the JSON object with event details.

3. **Example**

    - **Login**

        ```sh
        curl -X POST "http://127.0.0.1:8000/api/login" -H "accept: application/json" -H "Content-Type: application/json" -d '{"username":"test","password":"test"}'
        ```

    - **Upload Photo**

        ```sh
        curl -X POST "http://127.0.0.1:8000/upload/photo/" -H "accept: application/json" -H "Authorization: Bearer <your_token>" -H "Content-Type: multipart/form-data" -F "file=@path_to_your_image.jpg"
        ```

    - **Get JSON Object**

        ```sh
        curl -X GET "http://127.0.0.1:8000/json-object" -H "accept: application/json" -H "Authorization: Bearer <your_token>"
        ```

## Files

### `free_food_monash.py`

Contains the core logic to process images using OCR and extract event details.

### `free_food_monash_api.py`

Defines the FastAPI application, including endpoints for user login, image upload, and retrieving event details.

### `user.py`

Manages user creation and authentication. Uses Pydantic for data validation and integrates with security functions.

### `security.py`

Provides security utilities for password hashing, verification, and JWT token generation.

### `requirements.txt`

Lists all the dependencies required for the project.

### `runtime.txt`

Specifies the Python runtime version to be used (Python 3.10.12).

### `Procfile`

Used for deployment to specify commands to be run by the application.

### `Aptfile`

Specifies system-level dependencies to be installed.

## Dependencies

- `fastapi==0.101.1`
- `mangum==0.17.0`
- `opencv_python==4.7.0.72`
- `passlib==1.7.4`
- `Pillow==10.0.0`
- `pydantic==1.10.10`
- `PyJWT==2.8.0`
- `pytesseract==0.3.10`
- `Requests==2.31.0`

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or issues, please contact [your-email@example.com].

---

You can copy and paste this content directly into your README.md file, and it will be properly formatted in Markdown.
