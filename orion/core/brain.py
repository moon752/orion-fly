
from orion.core.dispatcher import handle_command

# Add inside your message handler:
if text.startswith("/"):
    await handle_command(text)
