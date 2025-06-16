import os

PHASES = {
    7:  "tasks/auto_solver.py",
    8:  "sim/task_simulator.py",
    9:  "tasks/task_queue.json",
    10: "freelance/freelancer_manager.py",
    11: "freelance/profile_editor.py",
    12: "freelance/bidder.py",
    13: "security/ip_masking.py",
    14: "reports/daily_report.py",
    15: "storage/backup_manager.py",
    16: "core/self_updater.py",
    17: "core/admin_commands.py",
    18: "dashboard/terminal_ui.py",
}

def check_phases():
    print("🔍 Checking ORION Phase Completion:\n")
    for phase, path in PHASES.items():
        status = "✅ COMPLETE" if os.path.exists(path) else "❌ MISSING"
        print(f"Phase {phase:>2}: {status} — {path}")

if __name__ == "__main__":
    check_phases()
