from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from zipfile import ZipFile
from datetime import datetime
import os, shutil

def zip_storage():
    name = f"orion_backup_{datetime.now():%Y%m%d_%H%M}.zip"
    with ZipFile(name, "w") as z:
        for root, _, files in os.walk("orion/storage"):
            for f in files:
                z.write(os.path.join(root, f))
    return name

def upload(file_path):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    f = drive.CreateFile({"title": os.path.basename(file_path)})
    f.SetContentFile(file_path)
    f.Upload()
    print("✅  Uploaded", file_path)

if __name__ == "__main__":
    zip_path = zip_storage()
    upload(zip_path)
    shutil.move(zip_path, "orion/storage")
