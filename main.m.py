import os
import csv
from datetime import datetime, timezone

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NANSEN_API_KEY")

URL = "https://api.nansen.ai/api/v1/profiler/address/labels"

headers = {
    "apikey": API_KEY,
    "Content-Type": "application/json",
}

results = []

with open("data/addresses.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        address = row["address"].strip()

        payload = {
            "address": address,
            "chain": "ethereum",
            "pagination": {
                "page": 1,
                "per_page": 100,
            },
        }

        try:
            response = requests.post(
                URL,
                headers=headers,
                json=payload,
                timeout=30,
            )

            data = response.json()

            if response.status_code == 200:
                status = "success"
                error = ""
            else:
                status = "failed"
                error = data.get("code", "unknown_error")

            results.append({
                "address": address,
                "provider": "Nansen",
                "status": status,
                "error": error,
                "queried_at": datetime.now(timezone.utc).isoformat(),
            })

        except requests.exceptions.RequestException as e:
            results.append({
                "address": address,
                "provider": "Nansen",
                "status": "failed",
                "error": str(e),
                "queried_at": datetime.now(timezone.utc).isoformat(),
            })

with open("data/nansen_output.csv", "w", newline="") as file:
    fieldnames = [
        "address",
        "provider",
        "status",
        "error",
        "queried_at",
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)

print(f"Processed {len(results)} addresses.")
print("Output saved to data/nansen_output.csv")