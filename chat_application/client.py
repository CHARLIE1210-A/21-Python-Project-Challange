import socket
import threading
import logging

# ================= Logger Config =================
logging.basicConfig(
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)


HOST = "127.0.0.1"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            logger.info(f"Received: {message}")
        except:
            logger.error("Connecction lost.")
            client.close()
            break

def write_messages():
    while True:
        message = input("Enter message to send: ")
        client.send(message.encode())
        
threading.Thread(target=receive_messages).start()
threading.Thread(target=write_messages).start()
            