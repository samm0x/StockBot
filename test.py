import os
import asyncio
import httpx


API_KEY = os.environ.get("CMC_PRO_API_KEY")

BASE_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"


async def get_prices():
    if not API_KEY:
        print("Error: CMC_PRO_API_KEY تنظیم نشده است.")
        return None

    headers = {
        "X-CMC_PRO_API_KEY": API_KEY
    }

    params = {
        "id": "1,1027",
        "convert": "USD"
    }

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(
                BASE_URL,
                headers=headers,
                params=params
            )

            response.raise_for_status()
            result = response.json()

            return result["data"]

    except httpx.HTTPStatusError as e:
        print("خطای API:", e.response.status_code)
        print("جزئیات:", e.response.text[:1000])

    except httpx.RequestError as e:
        print("خطا در اتصال به اینترنت:", e)

    except (ValueError, KeyError) as e:
        print("خطا در پردازش پاسخ API:", e)

    return None


async def main():
    prices = await get_prices()

    if prices is None:
        return

    for coin in prices.values():
        name = coin["name"]
        symbol = coin["symbol"]
        price = coin["quote"]["USD"]["price"]
        change_24h = coin["quote"]["USD"]["percent_change_24h"]

        print("-" * 35)
        print(f"نام ارز: {name}")
        print(f"نماد: {symbol}")
        print(f"قیمت: ${price:,.2f}")
        print(f"تغییر قیمت ۲۴ ساعته: {change_24h:.2f}%")


if __name__ == "__main__":
    asyncio.run(main())