import socket

IP: str = socket.gethostbyname(socket.gethostname()) # Get the IP
PORT: int = 8080
ADDR: tuple = (IP, PORT) # the address
SIZE: int = 1024
FORMAT: str = "utf-8"

    

def main() -> None:
    print(f"[STARTING] Server is starting at port {PORT}.")

    # Starting a TCP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the IP and PORT to the server
    server.bind(ADDR)

    # Server is listening, i.e., server is now waiting for the client to connected
    server.listen()
    print(f"[LISTENING] Server is listening at port {PORT}.")
    # infinite loop, the server always listens
    while True:         
        # Server has accepted the connection from the client
        conn, addr = server.accept()
        print("============================================")
        print(f"[NEW CONNECTION] {addr} connected.")

        # Receiving the filename from the client
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the filename.")
        file = open(filename, "w")
        conn.send("Filename received.".encode(FORMAT))

        # Receiving the file data from the client
        file_data = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the file data.")
        file.write(file_data)
        conn.send("File data received".encode(FORMAT))

        """ Closing the file. """
        file.close()

        """ Closing the connection from the client. """
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")
        print("============================================")

if __name__ == "__main__":
    main()

