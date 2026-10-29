import os
import httpx
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()

API_KEY = os.getenv("CMC_PRO_API_KEY")
BASE_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"


async def get_prices(symbol: str):
    if not API_KEY:
        raise HTTPException(
            status_code=500,
            detail="CMC_PRO_API_KEY تنظیم نشده است."
        )

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(
                BASE_URL,
                headers={"X-CMC_PRO_API_KEY": API_KEY},
                params={
                    "symbol": symbol.upper(),
                    "convert": "USD"
                }
            )

            print("API STATUS:", response.status_code)

            response.raise_for_status()
            result = response.json()

            print("PRICE KEYS:",
                  list(result.get("data",{}).keys()))

            if "data" not in result:
                raise HTTPException(
                    status_code=502,
                    detail="Invalid API response"
                )

            print("API SUCCESS")

            return result["data"]

    except httpx.HTTPStatusError as e:
        print("API ERROR:", e.response.status_code, e.response.text)
        raise HTTPException(
            status_code=502,
            detail="CoinMarketCap API error"
        ) from e

    except httpx.RequestError as e:
        print("CONNECTION ERROR:", str(e))
        raise HTTPException(
            status_code=502,
            detail="Could not connect to CoinMarketCap"
        ) from e