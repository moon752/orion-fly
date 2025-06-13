import subprocess, logging, sys
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
def main():
    try:
        logging.info("🔄 Pulling latest code…")
        subprocess.run(["git", "pull"], check=True)
        logging.info("✅  Updated. Restarting ORION core.")
        subprocess.Popen([sys.executable, "-m", "orion_phase8_core"])
    except subprocess.CalledProcessError as e:
        logging.error("❌  Upgrade failed: %s", e)
if __name__ == "__main__":
    main()
