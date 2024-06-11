import os
import requests
from pypresence import Presence
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables or prompt the user
API_KEY = os.getenv('API_KEY')
if not API_KEY:
    API_KEY = input("Please enter your API key: ")

# Base URL for Onshape API
BASE_URL = 'https://cad.onshape.com/api'

# Discord client ID
DISCORD_CLIENT_ID = '1250116187732578354'

# Function to get headers with authentication
def get_headers():
    return {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Basic {API_KEY}'
    }

# Function to get user information
def get_user_info():
    url = f'{BASE_URL}/users/session'
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()

# Function to get all documents
def get_all_documents():
    url = f'{BASE_URL}/documents'
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()

# Function to find the most recently modified document
def find_active_document(documents):
    if 'items' not in documents:
        return None
    
    # Sort documents by last modified date
    sorted_documents = sorted(documents['items'], key=lambda x: x['modifiedAt'], reverse=True)
    return sorted_documents[0] if sorted_documents else None

# Initialize Discord Rich Presence
rpc = Presence(DISCORD_CLIENT_ID)
rpc.connect()

# Keep the presence updated
while True:
    try:
        user_info = get_user_info()
        user_name = user_info["name"]
        user_email = user_info["email"]
        
        all_documents = get_all_documents()
        
        active_document = find_active_document(all_documents)
        if active_document:
            document_name = active_document["name"]
            document_id = active_document["id"]
            last_modified = active_document["modifiedAt"]
            
            print(f'Active Document ID: {document_id}')
            print(f'Name: {document_name}')
            print(f'Last Modified: {last_modified}')
            
            # Update Discord Rich Presence with a button linking to the GitHub project
            rpc.update(
                state=f"Editing: {document_name}",
                details=f"User: {user_name}",
                large_image="onshape_logo",
                large_text="Onshape CAD",
                small_image="onshape_logo",  
                small_text="IIRoan/OnshapeDRPC",
                buttons=[{"label": "Onshape CAD", "url": "https://cad.onshape.com"}] 
            )
        else:
            print("No active document found.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    
    time.sleep(30)  # Wait for 30 seconds before the next API query
