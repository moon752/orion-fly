import multiprocessing
import time
import traceback
from orion.main import run_orion_once
from orion.utils.telegram_notify import notify_admin

def worker_loop(hive_id):
    notify_admin(f"🐝 Hive #{hive_id} started.")
    while True:
        try:
            run_orion_once(hive_id)
            time.sleep(10)
        except Exception as e:
            traceback.print_exc()
            notify_admin(f"⚠️ Hive #{hive_id} crashed:\n{e}")
            time.sleep(30)  # cooldown before restart

def spawn_hive(count=4):
    notify_admin(f"🚀 Launching {count} autonomous hives...")
    for i in range(count):
        p = multiprocessing.Process(target=worker_loop, args=(i,))
        p.daemon = True
        p.start()
