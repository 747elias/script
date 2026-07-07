import socket
import threading

# ==== Einstellungen ====
MODE = input("Modus wählen (server/client): ").strip()
PORT = 12345

# Nachricht empfangen
def receive_messages(conn):
    while True:
        try:
            msg = conn.recv(1024).decode()
            if msg:
                print(f"\n[Empfangen] {msg}\n> ", end="")
        except:
            print("\n[Verbindung getrennt]")
            break

# Nachricht senden
def send_messages(conn):
    while True:
        msg = input("> ")
        try:
            conn.send(msg.encode())
        except:
            print("[Nachricht konnte nicht gesendet werden]")
            break

if MODE == "server":
    HOST = "0.0.0.0"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"[Server] Warte auf Verbindung auf Port {PORT}...")
    conn, addr = server.accept()
    print(f"[Server] Verbunden mit {addr}")

elif MODE == "client":
    SERVER_IP = input("IP des Servers: ").strip()
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((SERVER_IP, PORT))
    print(f"[Client] Verbunden mit Server {SERVER_IP}:{PORT}")

else:
    print("Ungültiger Modus (nur 'server' oder 'client' erlaubt)")
    exit()

# Threads starten
recv_thread = threading.Thread(target=receive_messages, args=(conn,), daemon=True)
send_thread = threading.Thread(target=send_messages, args=(conn,), daemon=True)

recv_thread.start()
send_thread.start()

recv_thread.join()
send_thread.join()
