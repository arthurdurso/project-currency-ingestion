import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://api.freecurrencyapi.com/v1/latest"

response = requests.get(
    url,
    params={
        "apikey": os.getenv("SOURCES__SOURCE__FREECURRENCYAPI__API_KEY"),
        "base_currency": "BRL",
        "currencies": "USD,EUR,JPY"
    }
)



STATUS_CODE = response.status_code
data = response.json()

print("\nStatus Code:", STATUS_CODE)
print("\nData:", data)
