# Catalys Task - Flask Data Processing Application

This repository contains a Flask-based application designed for processing JSON data. The application reads JSON files from a directory, processes the data by converting text to uppercase, and calculates the total sum of all `price` fields within the JSON data. It exposes two API endpoints for fetching and retrieving the processed data.

## Features

- **Fetch JSON Data**: Retrieve JSON data from the `Mock_Data` directory.
- **Process Data**:
  - Convert all text values to uppercase.
  - Calculate the sum of all `price` fields within the JSON data.
- **Session Management**: Store and manage the fetched data in a session.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/MohamedImamrila/Catalys_Task.git
    cd Catalys_Task
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Directory Structure

Ensure the JSON files are placed in the `Mock_Data` directory. The structure should look like this:

```Catalys_Task/
├── app.py
├── Mock_Data/
│ ├── example1.json
│ ├── example2.json
│ └── ...
├── requirements.txt
└── README.md
```

## Running the Application

1. **Start the Flask application**:
    ```bash
    python app.py
    ```

2. **Access the API endpoints** using a tool like Postman, cURL, or a web browser:

   - **Fetch Data**:
     - **Endpoint**: `/fetch-data`
     - **Method**: `GET`
     - **Description**: Fetches and stores JSON data from the `Mock_Data` directory into the session.

   - **Processed Data**:
     - **Endpoint**: `/processed-data`
     - **Method**: `GET`
     - **Description**: Retrieves the processed data, which includes:
       - All text fields converted to uppercase.
       - The total sum of all `price` fields in the JSON data.

## Configuration

- **Secret Key**: The session management uses a secret key (`'catalys'`) for security purposes.
- **Session Lifetime**: Sessions are set to be permanent with a lifetime of 60 seconds.

## Example JSON File Structure

An example of how the JSON files in the `Mock_Data` directory should be structured:

```json
{
    "item": "Sample Item",
    "price": "20.50",
    "details": {
        "description": "This is a sample description.",
        "category": "Sample Category"
    }
}
