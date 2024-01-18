from socket import socket, AF_INET, SOCK_STREAM

# Server configuration
server_ip = "127.0.0.1"
server_port = 8888

def start_vpn_client():
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    message = "Hello, VPN Server! Made By - Aryan || Guide - Krashnakant Sir"
    client_socket.send(message.encode())
    client_socket.close()

if __name__ == '__main__':
    start_vpn_client()
