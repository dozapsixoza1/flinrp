#!/usr/bin/env python3
"""Conservative static inspection of a decoded Flinity APK package."""
from pathlib import Path
import re
import sys

root = Path(sys.argv[1])
needles = (b"setClientIp", b"setClientPort", b"195.18.27.226", b"FLINITY", b"FLIN MOBILE")
print("FLIN RP launcher package inspection")
for path in sorted(root.rglob("*")):
    if not path.is_file():
        continue
    try:
        data = path.read_bytes()
    except OSError:
        continue
    found = [item.decode() for item in needles if item in data]
    if found:
        print(f"{path.relative_to(root)}: {', '.join(found)}")

for dex in sorted(root.glob("classes*.dex")):
    data = dex.read_bytes()
    for method in (b"setClientIp", b"setClientPort"):
        offsets = [match.start() for match in re.finditer(re.escape(method), data)]
        if offsets:
            print(f"{dex.name}: {method.decode()} string-id offsets={offsets[:8]}")

print("\nDEX string matches do not prove the active connection configuration.")
print("Do not replace arbitrary addresses: the launcher may load its server list remotely.")
