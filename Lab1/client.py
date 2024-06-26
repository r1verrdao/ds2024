import socket

IP: str = socket.gethostbyname(socket.gethostname()) # Get the IP
PORT: int = 8080
ADDR: tuple = (IP, PORT) # the address
SIZE: int = 1024
FORMAT: str = "utf-8"

FILENAME: str = "file.txt"

def main():
    # Create TCP socket for client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client.connect(ADDR)

    # Open and send the file
    f = open(FILENAME, "r")
    file_data = f.read()

    # Firstly: sending the filename to the server
    client.send(FILENAME.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    # Then, we send the data of the file to the server
    client.send(file_data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    #close the file
    f.close()

    # When sending the file is finished, close the connection
    client.close()



if __name__ == "__main__":
    main()