import socket
import json
import math
import os


file_name = input('enter file name to share')
filename = (file_name + ".png")
c = os.path.getsize(filename)
CHUNK_SIZE = math.ceil(math.ceil(c)/5)                                                           #size of chunks
file_number = 1
with open(filename, 'rb') as f:                                               #open file as binary file
    chunk = f.read(CHUNK_SIZE)
    while chunk:                                                               #while data left
        with open("filedirectory/" + file_name + "_" + str(file_number) ,'wb') as chunk_file:      #open new file and save chunk to there
            chunk_file.write(chunk)
        file_number += 1
        chunk = f.read(CHUNK_SIZE)

chunk_file.close()
print ('ready to host: ' + str(file_name))

PORT = 5001
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', PORT))
server_socket.listen(6)                                    #3 is supported number of connections
while 1:
    print("Waiting for incoming connection...")
    connection_socket, IP = server_socket.accept()
    recived_dictionary = connection_socket.recv(2000)
    requested_chunk_name = json.loads(recived_dictionary)
    chunk_name = requested_chunk_name['filename']
    chunk_name = "filedirectory/" + chunk_name
    with open(chunk_name,'rb') as f:
        data = f.read(CHUNK_SIZE)
        connection_socket.send(data)
    # connection_socket.close()















