import socket
import json

def main():
    """
    Connects to a server, sends a search request, and prints the results.
    """
    host = "127.0.0.1"
    port = 1455

    filename = input("Enter a filename: ")
    word = input("Enter the word to search: ")

    request_data = {
        'filename': filename,
        'word' : word
    }
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(json.dumps(request_data).encode())
        response_data = s.recv(1024)

    result = json.loads(response_data)
    print("Search Results: ", result)


if __name__ == "__main__":
    main()
