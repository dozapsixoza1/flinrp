#!/usr/bin/env python3
import hashlib
import pathlib
import re
import subprocess
import sys

path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "libsamp.so")
if not path.is_file() or path.stat().st_size == 0:
    raise SystemExit("ERROR: libsamp.so is missing or empty")

def run(*args):
    return subprocess.run(args, check=True, text=True, capture_output=True).stdout

data = path.read_bytes()
header = run("readelf", "-h", str(path))
dynamic = run("readelf", "-d", str(path))
symbols = run("readelf", "-Ws", str(path))
machine = re.search(r"Machine:\s*(.+)", header)
elf_class = re.search(r"Class:\s*(.+)", header)
needed = re.findall(r"Shared library: \[(.*?)\]", dynamic)
exports = []
for line in symbols.splitlines():
    if " GLOBAL " in line and " DEFAULT " in line and not line.rstrip().endswith(" UND"):
        name = line.split()[-1]
        if name != "0":
            exports.append(name)

print("# FLIN RP native library report")
print()
print(f"- File: {path.name}")
print(f"- Size: {len(data)} bytes")
print(f"- SHA-256: {hashlib.sha256(data).hexdigest()}")
print(f"- ELF class: {elf_class.group(1).strip() if elf_class else 'unknown'}")
print(f"- Machine: {machine.group(1).strip() if machine else 'unknown'}")
print()
print("## Required shared libraries")
print("\n".join(f"- {x}" for x in needed) if needed else "- None reported")
print()
print("## Relevant exported symbols")
matches = [x for x in sorted(set(exports)) if any(k in x.lower() for k in ("clientip", "clientport", "samp", "jni"))]
print("\n".join(f"- {x}" for x in matches[:200]) if matches else "- No matching exported names found")
print()
print("## Full ELF header")
print("    " + header.replace("\n", "\n    "))
