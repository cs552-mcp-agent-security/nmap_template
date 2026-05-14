#!/usr/bin/env python3
import ipaddress
import socket
import sys

ALLOWED_HOSTS = {"localhost", "127.0.0.1", "::1"}

def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_target.py <host-or-ip>", file=sys.stderr)
        return 2
    target = sys.argv[1].strip()
    if target in ALLOWED_HOSTS:
        return 0
    try:
        ip = ipaddress.ip_address(target)
    except ValueError:
        try:
            resolved = socket.gethostbyname(target)
            ip = ipaddress.ip_address(resolved)
        except Exception:
            print(f"Could not resolve target: {target}", file=sys.stderr)
            return 2
    if ip.is_loopback:
        return 0
    print(f"Refusing non-local target: {target}", file=sys.stderr)
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
