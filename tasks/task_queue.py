import sqlite3, json, pathlib, time
DB="tasks/queue.db"; pathlib.Path("tasks").mkdir(exist_ok=True)
conn=sqlite3.connect(DB)
conn.execute("""CREATE TABLE IF NOT EXISTS queue(
 id INTEGER PRIMARY KEY, task TEXT, status TEXT, ts REAL)""")
def add(task): conn.execute("INSERT INTO queue(task,status,ts) VALUES(?,?,?)",(json.dumps(task),"new",time.time())); conn.commit()
def pop():
    cur=conn.execute("SELECT id,task FROM queue WHERE status='new' ORDER BY ts LIMIT 1").fetchone()
    if cur: conn.execute("UPDATE queue SET status='busy' WHERE id=?", (cur[0],)); conn.commit()
    return cur
def done(id_): conn.execute("UPDATE queue SET status='done' WHERE id=?", (id_,)); conn.commit()
