
import socket
from datetime import datetime

print("=== AVAIR Python Test ===")
print(f"Device: {socket.gethostname()}")
print(f"Time: {datetime.now().isoformat(timespec='seconds')}")
print("STATUS: Updated on BLACKBOX and executed on AVAIR!")
