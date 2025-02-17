import os

import dotenv
import resend

dotenv.load_dotenv()
resend.api_key = os.environ["RESEND_API_KEY"]

params: resend.Emails.SendParams = {
    "from": "Test <test@resend.dev>",
    "to": ["tqtien@croft-ai.com"],
    "subject": "hello world",
    "html": "<strong>it works!</strong>",
}

email = resend.Emails.send(params)
print(email)
