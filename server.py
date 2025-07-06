import http.server
import socketserver
import os

# Configuration
HOST = "192.168.1.54"  # Ton IP locale (remplace si besoin)
PORT = 5000
DIRECTORY = "."

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        print("[LOG] %s - - %s" % (self.client_address[0], format % args))

# Se placer dans le bon dossier
os.chdir(DIRECTORY)

with socketserver.TCPServer((HOST, PORT), MyHandler) as httpd:
    print(f"🟢 Serveur accessible à : http://{HOST}:{PORT}")
    print("📁 Dossier racine :", os.path.abspath(DIRECTORY))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🔴 Serveur arrêté.")
        httpd.server_close()
