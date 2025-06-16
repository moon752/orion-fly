import asyncio
from orion_phase8_core import run_orion

async def spawn(n):
    print(f"🐝  ORION node {n} online")
    await run_orion()

async def main():
    await asyncio.gather(*(spawn(i) for i in range(5)))  # 5-node hive

if __name__ == "__main__":
    asyncio.run(main())
