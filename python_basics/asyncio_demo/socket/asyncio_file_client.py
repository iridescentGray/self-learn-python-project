import socket

client = socket.socket()
client.connect(("localhost", 9999))

with open("test_file", "rb") as f:
    client.sendfile(f)
