import asyncio

async def job_search_loop():
    while True:
        # Call job search and proposal functions
        print("Searching jobs...")
        await asyncio.sleep(3600)  # every hour

async def start_scheduler():
    await asyncio.gather(job_search_loop())

# To run in main.py: asyncio.run(start_scheduler())
