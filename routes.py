import json
import redis.exceptions
from fastapi import APIRouter, HTTPException
from servece.price_service import get_prices
from redis_client import redis_client

router = APIRouter()


@router.get("/Prices")
async def get_crypto_prices(name: str):
    name = name.strip().upper()

    if not name:
        raise HTTPException(
            status_code=400,
            detail="Crypto symbol cannot be empty"
        )

    try:
        cached_data = await redis_client.get(name)
        if cached_data:
            return json.loads(cached_data)
    except redis.exceptions.RedisError:
        pass

    try:
        async with redis_client.lock(f"lock:{name}", timeout=10):
            cached_data = await redis_client.get(name)
            if cached_data:
                return json.loads(cached_data)

            prices = await get_prices(name)

            if name not in prices:
                raise HTTPException(
                    status_code=404,
                    detail="Crypto prices not found"
                )

            crypto = prices[name]
            coin = {
                "name": crypto["name"],
                "price": round(crypto["quote"]["USD"]["price"], 2)
            }

            await redis_client.setex(
                name,
                60,
                json.dumps(coin)
            )

            return coin

    except redis.exceptions.RedisError:
        prices = await get_prices(name)

        if name not in prices:
            raise HTTPException(
                status_code=404,
                detail="Crypto prices not found"
            )

        crypto = prices[name]

        return {
            "name": crypto["name"],
            "price": round(crypto["quote"]["USD"]["price"], 2)
        }