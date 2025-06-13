import sqlite3, random, os, json, math
DB="sim/econ.db"; os.makedirs("sim", exist_ok=True)
conn=sqlite3.connect(DB); cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS stats(job TEXT PRIMARY KEY, wins INT, losses INT)")
def beta_sample(a,b):       # std‑lib Thompson sample
    return random.betavariate(a,b)
def thompson_pick(job):
    cur.execute("SELECT wins,losses FROM stats WHERE job=?", (job,))
    w,l = cur.fetchone() or (0,0)
    return beta_sample(w+1, l+1)
def record(job, success):
    cur.execute("INSERT OR IGNORE INTO stats(job,wins,losses) VALUES(?,?,?)",(job,0,0))
    cur.execute(f"UPDATE stats SET {'wins' if success else 'losses'}={'wins' if success else 'losses'}+1 WHERE job=?", (job,))
    conn.commit()
def simulate_batch():
    jobs=["Python","Web","Writing","AI"]
    picked=max(jobs, key=thompson_pick)
    success=random.random()<0.6
    record(picked, success)
    print(json.dumps({"picked":picked,"success":success}))
if __name__=="__main__":
    for _ in range(10): simulate_batch()
