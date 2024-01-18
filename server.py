from OpenSSL import SSL
from socket import socket, AF_INET, SOCK_STREAM

# Server configuration
server_ip = "127.0.0.1"
server_port = 8888

def handle_client(client_socket):
    while True:
        data = client_socket.recv(4096)
        if not data:
            break
        print(f"Received from client: {data.decode()}")
        # Add your VPN-like logic here

def start_vpn_server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print(f"[*] VPN Server listening on {server_ip}:{server_port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        handle_client(client_socket)

if __name__ == '__main__':
    start_vpn_server()
