import asyncio

async def bew_chai():
    print("Brewing chai ...")
    await asyncio.sleep(2)
    print("Chai is ready")

asyncio.run(bew_chai())