# Using the API with Python Requests Library

This README provides instructions on how to use the API implemented in Django with the Python `requests` library. The API is designed to answer questions based on given abstracts fetched from an external source using Groq.

## Prerequisites

Before using the API, ensure you have the following prerequisites installed:

- Python 3.x
- Django
- Python `requests` library

## Getting Started

1. Clone the repository containing the Django project with the API implementation.

2. Navigate to the directory containing the Django project.

3. Start the Django development server:
   ```
   python manage.py runserver
   ```

4. The server should now be running locally at `http://127.0.0.1:8000/`.

## Using the API

To use the API, follow these steps:

1. Open a new Python script or interactive Python shell.

2. Import the `requests` library:
   ```python
   import requests
   ```

3. Send a POST request to the API endpoint (`/answer/`) with the required parameters: question, keywords, and num_results. Here's an example:
   ```python
   url = 'http://127.0.0.1:8000/answer/'
   data = {
       'question': 'What are the symptoms of COVID-19?',
       'keywords': 'COVID-19 symptoms',
       'num_results': 3
   }

   response = requests.post(url, data=data)

   if response.status_code == 200:
       print("API response:", response.json())
   else:
       print("Failed to fetch response from the API. Status code:", response.status_code)
   ```

4. Replace the `question` and `keywords` values with your desired question and search keywords. Adjust the `num_results` parameter as needed.

5. Run the Python script or execute the code snippet in your interactive Python shell.

6. Check the output to see the API response.

## Additional Notes

- Ensure that the Django development server is running locally before sending requests to the API.
- Handle errors and edge cases appropriately in your code, such as checking for invalid responses or network errors.
- For production use, deploy the Django project to a suitable hosting environment and update the API endpoint accordingly.
