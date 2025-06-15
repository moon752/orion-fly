import shutil, datetime, os
def backup():
    fname = f"backup_{datetime.datetime.utcnow().isoformat()}.zip"
    shutil.make_archive(fname, 'zip', ".")
    print("Backup created:", fname)
