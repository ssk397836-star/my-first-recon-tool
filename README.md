# My First Recon Tool - by 0xRaj
import socket
print("=== 0xRaj Recon Tool v1.0 ===")
target = input("Enter website (e.g., google.com): ")
try:
    ip = socket.gethostbyname(target)
    print(f"\n[+] Target: {target}")
    print(f"[+] IP Address: {ip}")
    print(f"[+] Scan Complete!")
except:
    print("[-] Could not find IP.")
