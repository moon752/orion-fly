import subprocess, builder.test_runner as tr
def main():
    if not tr.run():
        print("❌ Abort push — tests failed.")
        return
    subprocess.run(["git","add","-A"])
    subprocess.run(["git","commit","-m","🤖 auto_build upgrade"], check=False)
    subprocess.run(["git","push","origin","main"], check=False)
    print("🚀 Code pushed.")
if __name__=="__main__":
    main()
