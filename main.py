import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NANSEN_API_KEY")

address = "0xB809888f88ed90f4990149c85C4F661b5a8e35EE"

url = "https://api.nansen.ai/api/v1/profiler/address/labels"

headers = {
    "apikey": API_KEY,
    "Contract-Type": "application/json",
}

payload = {
    "address": address,
    "chain": "ethereum",
    "pagination": {
        "page": 1,
        "per_page": 100
    }
}

try:
    response  = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=30
    )

    data = response.json()

    if response.status_code == 200:
        print("API request successful.")
        print(data)

    elif response.status_code == 403:
        print("API request rejected")
        print("HTTP Status:", response.status_code)

        error_code = data.get("code")

        if error_code == "insufficient_credits":
            print("Reason: Insufficient Nansen API credits.")
        else:
            print("Reason:", data.get("message"))

    else:
        print("API request failed.")
        print("HTTP Status:", response.status_code)
        print("Response:", data)

except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.RequestException as error:
    print("Network error:", error)