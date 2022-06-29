# Conversational Agent for German national parks

Project for Conversational AI Workshop at TUM [sebis](https://wwwmatthes.in.tum.de/pages/t5ma0jrv6q7k/sebis-Public-Website-Home).

## Prerequisites

- Dialogflow account
- python>=3.8
- [ngrok](https://ngrok.com/) (for local development)

## Setup

Clone this repo, navigate to the root directory, and execute the following commands

```{bash}
python3 -m pip install --user virtualenv
python3 -m venv dialogflow-venv
source dialogflow-venv/bin/activate
pip3 install -r requirements.txt
```

### ngrok setup for local development

1. Register for ngrok at https://dashboard.ngrok.com/signup.
1. Find your authentication token at https://dashboard.ngrok.com/get-started/your-authtoken.
1. Copy the token and execute

   ```{bash}
   ngrok config add-authtoken [TOKEN]
   ```

## Local development

1. `python3 run.py`. Make sure that the Flask app is running on localhost port 8000.
1. `ngrok http 8000`.
1. Go to Dialogflow and paste the forwarding URL to Diagflow -> Fulfilment -> Webhook -> URL.
