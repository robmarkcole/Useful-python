import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# Python 3.7+
if __name__ == "__main__":
    asyncio.run(main())