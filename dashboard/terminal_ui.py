from brain.self_awareness import get_system_status
def show():
    print("=== ORION DASHBOARD ===")
    print(get_system_status())
if __name__ == "__main__":
    show()
