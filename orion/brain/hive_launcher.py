from orion.brain.hive_control import spawn_hive
from orion.utils.telegram_notify import notify_admin
from orion.monitor.dashboard import launch_dashboard
from orion.brain.client_bridge import handle_incoming_clients

notify_admin("🚀 ORION Hive Control Activated.")
launch_dashboard()
handle_incoming_clients()
spawn_hive(count=5)
from orion.stealth.cloaker import cloak_identity
cloak_identity("Account_1")
cloak_identity("Account_2")
cloak_identity("Account_3")
cloak_identity("Account_4")
cloak_identity("Account_5")
