# SignMate-ml-backend

**SignMate-ml-backend** is the machine learning model backend for **SignMate**, designed to convert sign language videos into text. This backend uses a trained model to process videos and output corresponding text for enhanced accessibility.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

---

## Features

1. **Sign Video Processing**:
   - Converts sign language video input into textual output.
   
2. **REST API**:
   - Exposes endpoints to interact with the model.

3. **Fast and Scalable**:
   - Built using FastAPI, ensuring quick responses and scalability.

---

## Installation

### Prerequisites

Ensure the following tools are installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- [pip](https://pip.pypa.io/en/stable/)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/avijit969/SignMate-ml-backend.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd SignMate-ml-backend
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

---

## Usage

1. **Start the Server**:
   The FastAPI server will be running at `http://localhost:8000`.

2. **Upload Sign Video**:
   Use the `/upload` API endpoint to upload sign language videos for processing.

3. **Receive Text Output**:
   The backend processes the video and returns the textual conversion as a response.

---

## Technologies Used

- **Python**: Core programming language.
- **FastAPI**: For creating the REST API.
- **Machine Learning**: Pretrained model for video to text conversion.
- **Uvicorn**: For ASGI server.

---

## API Endpoints

- **POST /upload**: Upload a video file for processing.
    - **Request Body**: `file` (video file)
    - **Response**: JSON object with the converted text.
  
- **GET /status**: Check the API status.

---

## Contributing

1. **Fork the repository**.
2. **Create a new branch** for your feature.
3. **Commit your changes**.
4. **Submit a pull request**.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Contact

For any questions or support, reach out:

- **Email**: abhijitpradhan909@gmail.com
- **Website**: [SignMate]()