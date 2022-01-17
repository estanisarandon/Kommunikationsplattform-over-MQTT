import socket
import threading
import queue

HOST = "127.0.8.1"
PORT = 9876


def client_handler(client_socket, broadcast_queue):
    while True:
        # Get data from client, BLOCKING
        message = client_socket.recv(1024)
        message = message.decode('utf-8')
        print("Got message", message)

        # Create a dictionary that contains the socket
        # used to receive the message, and the message
        message_dict = {
            'sender_socket': client_socket,
            'message': message.encode('utf-8')
        }
        # Add the dictionary to the broadcast queue
        broadcast_queue.put(message_dict)


def broadcast(client_list, broadcast_queue):
    print("Broadcast thread started")
    while True:
        # Wait for a message to broadcast
        message_dict = broadcast_queue.get()
        print("Broadcast thread for a message to send")
        for client in client_list:
            if client != message_dict['sender_socket']:
                client.send(message_dict['message'])


def main():
    # Create a socket that uses ip4 (AF_INET), and TCP (SOCK_STREAM)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))

    server_socket.listen()
    # Create a list of all connected clients
    client_list = []

    # Create a queue for communication between the client threads and the broadcast thread
    broadcast_queue = queue.Queue()

    # Start the broadcast thread. The client_list is mutable, so the thread and the main thread
    # will use the same list, not a copy
    broadcast_thread = threading.Thread(target=broadcast, args=(client_list, broadcast_queue))
    broadcast_thread.start()
    while True:
        # Wait for connection, BLOCKING
        client_socket, client_address = server_socket.accept()
        print(f'Client connect from {client_address}')
        # Start thread for client
        client_thread = threading.Thread(target=client_handler, args=(client_socket, broadcast_queue))
        # Add the new client_socket to the list of clients
        client_list.append(client_socket)
        client_thread.start()


if __name__ == '__main__':
    main()