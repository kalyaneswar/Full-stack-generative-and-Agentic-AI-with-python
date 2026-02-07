import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt(data):
    print(f"Lock {data[::-1]} ")

# encrypt("card123")

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        results = await loop.run_in_executor(pool, encrypt, "credit_card_1234")
        print(f"{results}")
    
if __name__ == "__main__":
    asyncio.run(main())

# asyncio.run(main())