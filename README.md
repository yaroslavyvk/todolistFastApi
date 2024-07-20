# ToDo List Application

This project is a simple ToDo List application built with FastAPI. It allows creating, reading, updating, and deleting tasks (CRUD operations).

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/todolist-fastapi.git
    cd todolist-fastapi
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

Run the server using Uvicorn:

```bash
uvicorn main:app --reload