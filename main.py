import os
from typing import Dict

import dotenv
import resend
from fastapi import FastAPI

dotenv.load_dotenv()
resend.api_key = os.environ["RESEND_API_KEY"]

app = FastAPI()


@app.post("/")
def send_mail() -> Dict:
    params: resend.Emails.SendParams = {
        "from": "Test <test@example.com>",
        "to": ["me@example.com"],
        "subject": "hello world",
        "html": "<strong>it works!</strong>",
    }

    email: resend.Email = resend.Emails.send(params)
    return dict(email)
