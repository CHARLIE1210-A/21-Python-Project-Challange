import socket
import threading
import logging

# ================= Logger Config =================
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

# ================= Server Config=================
HOST = "127.0.0.1"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)
            

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            clients.remove(client)
            client.close()
            break

logger.info("Starting server...")
while True:
    client, addr = server.accept()
    logger.info(f"New connection from {addr}: Connected.")
    
    clients.append(client)
    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()