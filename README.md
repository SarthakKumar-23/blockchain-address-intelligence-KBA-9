# Blockchain Address Intelligence — Nansen

A Python-based blockchain intelligence pipeline that demonstrates how Ethereum
addresses can be enriched using the Nansen API.

## Objective

The goal is to take a list of Ethereum addresses and query Nansen's address
intelligence API for address labels.

This project is intended for learning and portfolio demonstration. Nansen
labels and classifications are treated as third-party intelligence and are
not considered absolute facts.

## Data Source

**Provider:** Nansen API

**Endpoint:**

```text
POST /api/v1/profiler/address/labels
```

## Chain
```
Ethereum
```

## Pipeline
```
Ethereum Address List
        |
        v
addresses.csv
        |
        v
Python API Client
        |
        v
Nansen Address Labels API
        |
        v
API Response
        |
        v
Structured CSV Output
```

## Project Structure
blockchain-address-intelligence/<br>
│<br>
├── data/<br>
│   ├── addresses.csv<br>
│   └── nansen_output.csv<br>
│<br>
├── .env<br>
├── .gitignore<br>
├── main.m.py<br>
└── README.md<br>