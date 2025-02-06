import ngrok
import time
from dotenv import load_dotenv

load_dotenv()

listener = ngrok.forward(
    "http://127.0.0.1:8000",
    authtoken_from_env=True,
    basic_auth="",
    domain="read from env",
)
# listener = ngrok.forward("http://127.0.0.1:8000", authtoken_from_env=True, domain="example.ngrok.app")

print(f"Ingress URL: {listener.url()}")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    listener.close()
    print("Closed")
