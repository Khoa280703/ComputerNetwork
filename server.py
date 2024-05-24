import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen(5)

connected_clients = {}  # Use a dictionary to store connected clients' sockets

while True:
    client_socket, addr = server_socket.accept()
    pid = client_socket.recv(1024).decode()
    
    if pid == "exit":
        disconnected_pid = None
        for pid, sock in connected_clients.items():
            if sock == client_socket:
                disconnected_pid = pid
                break
        
        if disconnected_pid:
            connected_clients.pop(disconnected_pid)  # Remove the disconnected client
            print(f"Disconnected client: {disconnected_pid}")
    else:
        connected_clients[pid] = client_socket  # Add the connected client
        print(f"List of connected clients: {list(connected_clients.keys())}")
    
    client_socket.close()
