# Onshape Discord Rich Presence Integration

This project integrates Onshape API with Discord Rich Presence to display the user's current CAD project and username on Discord. It fetches the user's active document from Onshape and updates their Discord status to reflect the document they are currently editing.

## Features

- Fetches user information and active CAD project from Onshape.
- Displays the current CAD project name and user's name on Discord status.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have a Discord account.
- You have an Onshape account and have generated an API key.

## Setup Instructions

### Clone the Repository

Clone the repository using the following command:

```git clone https://github.com/Onshape-Public/onshape-discord-rpc.git``` \
```cd onshape-discord-rpc```


### Create and Activate a Virtual Environment

Create a virtual environment to manage the dependencies:
	
``` python -m venv venv```

Linux/MacOS:
```venv/bin/activate ```

Windows:
```venv\Scripts\activate ```


### Install Dependencies

Install the required Python packages:

```pip install -r requirements.txt```


### Environment Configuration

Create a `.env` file in the root directory of the project and add your 
Onshape API key:
please note that the API key you get from Onshape isnt base64 encoded, you need to encode it yourself please read 
https://onshape-public.github.io/docs/auth/apikeys/

``` API_KEY='your_base64_encoded_api_key'```


### Run the Application

Execute the script to start the application:

``` python main.py```


## Additional Information

- The application updates the Discord status every 15 seconds to reflect any changes in the active document.

