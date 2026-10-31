⚡ StockBot — Cryptocurrency Price API

An asynchronous cryptocurrency price API built with FastAPI, Redis, and Python.

Designed to retrieve cryptocurrency market prices efficiently while reducing unnecessary external API requests through caching.

🚀 Features

⚡ FastAPI — High-performance REST API.

📊 CoinMarketCap Integration — Cryptocurrency price retrieval.

🔄 Async HTTP Requests — Non-blocking requests using HTTPX.

⚡ Redis Caching — 60-second cache expiration.

🛡️ Request Coordination — Redis-based locking to help prevent duplicate concurrent requests.

📖 Swagger UI — Interactive API documentation.

🛠️ Tech Stack

Python · FastAPI · Redis · HTTPX · Uvicorn · CoinMarketCap API

📡 API Usage

Endpoint

GET /Prices?name=BTC 

Example Response

{ "name": "BTC", "price": 110000.00 } 

Example price for demonstration purposes only.

⚙️ Getting Started

Clone the repository.

Install dependencies:

pip install -r requirements.txt 

Configure the required environment variables.

Start Redis.

Run the FastAPI application using your project's configured entry point.

Open http://127.0.0.1:8000/docs to explore the API.

🔐 Security

Keep API keys in environment variables.

Never commit .env files or credentials to GitHub.

🎯 Project Focus

Demonstrates practical backend development through asynchronous API design, third-party service integration, Redis caching, and efficient data retrieval.

Built with Python. Designed for efficient cryptocurrency data access.