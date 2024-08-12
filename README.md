# Flask Data Processing Application

This is a Flask-based application that retrieves JSON data from files, processes the data, and provides API endpoints to fetch the original and processed data.

## Features

- Fetch JSON data from a specified directory.
- Process data by converting all text to uppercase.
- Calculate the sum of all `price` fields in the JSON data.
- Store data in a session for processing.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install Flask
    ```

## Usage

1. **Place your JSON files in the `Mock_Data` directory.** Ensure the directory structure is as follows:

    ```
    your-repo-name/
    ├── app.py
    ├── Mock_Data/
    │   ├── file1.json
    │   ├── file2.json
    │   └── ...
    └── ...
    ```

2. **Run the Flask application:**
    ```bash
    python app.py
    ```

3. **Access the endpoints:**

    - **Fetch JSON Data:**
      ```http
      GET /fetch-data
      ```
      This endpoint retrieves all JSON data from the `Mock_Data` directory and stores it in the session.

    - **Get Processed Data:**
      ```http
      GET /processed-data
      ```
      This endpoint processes the JSON data by converting text to uppercase and summing all `price` fields, then returns the processed data.

## API Endpoints

- **`GET /fetch-data`**: Fetches and stores all JSON data from the `Mock_Data` directory in the session.

- **`GET /processed-data`**: Returns the processed data, including all text in uppercase and the sum of all `price` fields.

## Configuration

- **Session Management:**
  - The session is configured with a secret key (`'catalys'`).
  - The session is set to be permanent with a lifetime of 60 seconds.

## Example JSON File Structure

Here is an example of how your JSON files might be structured:

```json
{
    "item": "Example Item",
    "price": "10.99",
    "details": {
        "description": "A sample description",
        "category": "Sample Category"
    }
}
