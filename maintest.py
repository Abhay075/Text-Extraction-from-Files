import requests




def upload_file(file_path: str, api_url: str):
   """
   Upload a file to the FastAPI endpoint for text extraction and processing.


   Args:
       file_path (str): Path to the file to be uploaded.
       api_url (str): URL of the FastAPI endpoint.


   Returns:
       dict: JSON response from the API.
   """
   try:
       # Open the file in binary mode
       with open(file_path, "rb") as file:
           # Prepare the files payload
           files = {"file": file}
           # Make the POST request
           response = requests.post(api_url, files=files)


       # Check the response status code
       if response.status_code == 200:
           print("Success! Response:")
           return response.json()
       else:
           print(f"Error: {response.status_code} - {response.text}")
           return None


   except Exception as e:
       print(f"test.py: {str(e)}", flush=True)
       return None




if __name__ == "__main__":
   API_URL = "http://127.0.0.1:8000/process-file"


   # Path to the file to upload
   # file_path = "img.png"
   file_path = "pic.png"


   # Call the upload_file function
   result = upload_file(file_path, API_URL)


   if result:
       # Print the API's JSON response
       print(result)
