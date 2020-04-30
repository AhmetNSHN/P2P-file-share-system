import socket
import json

content_dictionary = { }
with open('content_dictionary.txt', 'r') as f:
    data = json.load(f)  # convert json file to object
content_dictionary = json.dumps(data)

file_name = input('enter file name to download:')
chunk_index = 1
chunk_name = file_name + "_" + str(chunk_index)
chunk_index = chunk_index + 1
requested_chunk = {"filename" : " "}
requested_chunk['filename'] = chunk_name

print(content_dictionary)
# s = socket.socket()
# host = input(str("Enter host adress:"))
# port = 5000
# s.connect((host,port))
# print("Connected...")
#
# filename = input(str("Enter filename:"))
# file = open(filename, 'wb')
# file_data = s.recv(1024)
# file.write(file_data)
# file.close()
# print("File has been received.")