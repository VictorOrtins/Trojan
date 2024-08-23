import socket
import base64
import random
from string import ascii_lowercase

# create TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# listen of localhost port 1337
s.bind(("127.0.0.1", 1337))

# queue up to 5 requests
s.listen(5)

print("Esperando informações na porta 1337...")

while True:
    # establish a connection
    clientsocket, client_ip = s.accept()
    print("[+] Recebi uma conexão de: {}".format(client_ip))

    # get the encoded data
    encoded_data = clientsocket.recv(10000)
    clientsocket.close()

    with open("".join(random.choices(ascii_lowercase, k=10)), "w") as random_fd:
        print(len(base64.b64decode(encoded_data).decode("UTF-8")))
        random_fd.write(base64.b64decode(encoded_data).decode("UTF-8"))
