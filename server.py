import socket
import json
from search import Search

def main():
    """
    Run a TCP server that listens for search requests, processes them,
    and sends back results.
    """
    host = "127.0.0.1"
    port = 1455
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((host, port))
        except s.error as err:
            print("Connection Failed", err)
            return
        print("Connecting...")
        s.listen()
        print("Server listening on port", port)

        while True:
            conn, addr = s.accept()
            with conn:
                print("Connected to ", addr)
                recieved_data = conn.recv(1024)
                if not recieved_data:
                    break
                
                response_data = search_the_result(recieved_data)
                conn.sendall(response_data)

def search_the_result(data):
    request = json.loads(data)
    filename = request['filename']
    word = request['word']

    search = Search(filename)
    search.clean()
    result = search.get_lines(word)
    return json.dumps(result).encode()

if __name__ == "__main__":
    main()
