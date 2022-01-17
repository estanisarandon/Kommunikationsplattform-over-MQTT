import socket
import threading

HOST = '127.0.8.1'
PORT = 9876

def input_handler(client_socket):
    while True:
        # Get user message - BLOCKING
        message = input("Enter something> ")
        # Send the message
        client_socket.send(message.encode('utf-8'))


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Create a thread and start it
    input_threading = threading.Thread(target=input_handler, args=(client_socket, ))
    input_threading.start()

    while True:
        # Receive message from server - BLOCKING
        message = client_socket.recv(1024).decode("utf-8")
        print(message)


if __name__ == '__main__':
    main()