import os
import sys
import socket
import hashlib
import qrcode
import random
import string
import speedtest as speedtestcli
import requests

# Farben für Konsole
R = '\033[91m'  # Rot
G = '\033[92m'  # Grün
Y = '\033[93m'  # Gelb
B = '\033[94m'  # Blau
C = '\033[96m'  # Cyan
W = '\033[0m'   # Weiß (Reset)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(f"""{R}
████████╗██████╗░  ████████╗░█████╗░░█████╗░██╗░░░░░
╚══██╔══╝██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
░░░██║░░░██████╦╝  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
░░░██║░░░██╔══██╗  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
░░░██║░░░██║░░██║  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
░░░╚═╝░░░╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
{W}
{R}Coded by IsaTR{W}
{Y}Version: 1               {C}CTRL+C to exit               {W}Author: IsaTR
""")

def menu():
    print(f"""{B}
[1]  IP-Scanner
[2]  Port Scanner
[3]  Hash Generator
[4]  QR Code Generator
[5]  Password Generator
[6]  Speedtest
[7]  Website Status Checker
[8]  Hostname zu IP
[9]  IP zu Hostname
[10] Zufälliger User-Agent
[11] Datei-Hasher (SHA256)
[12] HTTP-Header einer Website
[13] Öffentliche IP anzeigen
[14] IP-Locator
[15] Beenden
{W}""")

# Tool-Funktionen

def ip_scanner():
    ip = input("Gib eine IP ein: ")
    print(f"Pinge {ip} ...\n")
    os.system(f"ping -n 4 {ip}" if os.name == "nt" else f"ping -c 4 {ip}")

def port_scanner():
    target = input("Gib eine IP oder Domain ein: ")
    ports = [21, 22, 80, 443, 8080]
    print(f"Scanne Ports bei {target} ...\n")
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            sock.connect((target, port))
            print(f"{G}[+] Port {port} offen{W}")
            sock.close()
        except:
            print(f"{R}[-] Port {port} geschlossen{W}")

def hash_generator():
    text = input("Text zum Hashen: ")
    print("SHA256:", hashlib.sha256(text.encode()).hexdigest())

def qr_generator():
    data = input("Text oder URL für QR-Code: ")
    img = qrcode.make(data)
    img.save("qrcode.png")
    print("QR-Code gespeichert als qrcode.png")

def password_generator():
    try:
        length = int(input("Länge des Passworts: "))
        characters = string.ascii_letters + string.digits + string.punctuation
        pw = ''.join(random.choice(characters) for _ in range(length))
        print("Generiertes Passwort:", pw)
    except:
        print("Ungültige Eingabe!")

def speed_test():
    print("Starte Speedtest ...")
    st = speedtestcli.Speedtest()
    print("Download:", round(st.download() / 1_000_000, 2), "Mbps")
    print("Upload:  ", round(st.upload() / 1_000_000, 2), "Mbps")

def site_status():
    site = input("Website URL (mit http/https): ")
    try:
        r = requests.get(site, timeout=5)
        print(f"Status Code: {r.status_code}")
    except Exception as e:
        print(f"Fehler: {e}")

def host_to_ip():
    host = input("Hostname eingeben: ")
    try:
        print("IP:", socket.gethostbyname(host))
    except Exception as e:
        print(f"Fehler: {e}")

def ip_to_host():
    ip = input("IP-Adresse eingeben: ")
    try:
        print("Hostname:", socket.gethostbyaddr(ip)[0])
    except Exception as e:
        print(f"Fehler: {e}")

def random_user_agent():
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (X11; Linux x86_64)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X)",
    ]
    print("User-Agent:", random.choice(agents))

def file_hasher():
    path = input("Pfad zur Datei: ")
    try:
        with open(path, "rb") as f:
            print("SHA256:", hashlib.sha256(f.read()).hexdigest())
    except FileNotFoundError:
        print("Datei nicht gefunden!")

def get_headers():
    url = input("Website-URL: ")
    try:
        r = requests.get(url, timeout=5)
        for k, v in r.headers.items():
            print(f"{k}: {v}")
    except Exception as e:
        print(f"Fehler: {e}")

def public_ip():
    try:
        ip = requests.get("https://api.ipify.org").text
        print("Deine öffentliche IP:", ip)
    except:
        print("Fehler beim Abrufen der IP.")

def iplocater():
    try:
        ip = input("IP-Adresse eingeben: ")
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data['status'] == 'success':
            print(f"Land: {data['country']}")
            print(f"Region: {data['regionName']}")
            print(f"Stadt: {data['city']}")
            print(f"ISP: {data['isp']}")
            print(f"Organisation: {data['org']}")
            print(f"Koordinaten: {data['lat']}, {data['lon']}")
        else:
            print("Fehler: IP nicht gefunden.")
    except Exception as e:
        print(f"Fehler beim Abrufen: {e}")

# Main Loop

def main():
    while True:
        try:
            clear()
            banner()
            menu()
            choice = input("Wähle eine Option (1-15): ").strip()
            clear()
            banner()
            funcs = {
                "1": ip_scanner,
                "2": port_scanner,
                "3": hash_generator,
                "4": qr_generator,
                "5": password_generator,
                "6": speed_test,
                "7": site_status,
                "8": host_to_ip,
                "9": ip_to_host,
                "10": random_user_agent,
                "11": file_hasher,
                "12": get_headers,
                "13": public_ip,
                "14": iplocater,
                "15": sys.exit
            }
            if choice in funcs:
                funcs[choice]()
            else:
                print("Ungültige Auswahl!")
            input(f"\n{Y}Drücke Enter für Menü...{W}")
        except KeyboardInterrupt:
            print(f"\n{R}Manuell beendet.{W}")
            sys.exit()

if __name__ == "__main__":
    main()
