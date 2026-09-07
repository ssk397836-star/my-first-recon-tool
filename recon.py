
# My First Recon Tool v2.0 ULTIMATE - by 0xRaj
# Ethical Hacking - Educational Purpose Only

import socket

print("=== 0xRaj Recon Tool v2.0 ULTIMATE ===")
target = input("Enter website (e.g., google.com): ")

try:
    ip = socket.gethostbyname(target)
    print(f"\n[+] Target: {target}")
    print(f"[+] IP Address: {ip}")
    
    print("\n[+] Scanning common ports...")
    ports = [21, 22, 80, 443, 8080]
    for port in ports:
        s = socket.socket()
        s.settimeout(1)
        try:
            s.connect((ip, port))
            print(f"  [OPEN] Port {port}")
            # Banner Grabbing
            try:
                banner = s.recv(1024).decode().strip()
                print(f"         Banner: {banner}")
            except:
                pass
        except:
            print(f"  [CLOSED] Port {port}")
        s.close()
    
    print(f"\n[+] Scan Complete!")
    print("\nMade with ❤️ by 0xRaj")

except:
    print("[-] Could not find IP. Check website name.")