import socket
file_name = input('enter file name to share')
username = ('filedirectory/ahmet')
CHUNK_SIZE = 5000                                                              #size of chunks
file_number = 1
with open(file_name, 'rb') as f:                                               #open file as binary file
    chunk = f.read(CHUNK_SIZE)
    while chunk:                                                               #while data left
        with open(username + "_" + str(file_number) ,'wb') as chunk_file:      #open new file and save chunk to there
            chunk_file.write(chunk)
        file_number += 1
        chunk = f.read(CHUNK_SIZE)

chunk_file.close()

print ('ready to host: ' + str(file_name))


PORT = 5001
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("",PORT))
server_socket.listen(1)                                    #1 is supported number of connections
while 1:
    connection_socket, addr = server_socket.accept()
    sentence = connection_socket.recv(5000)
    # connection_socket.close()



# import socket
#
# s = socket.socket()
# host = socket.gethostname()
# port = 5000
# s.bind((host,port))
# s.listen(1)
# print(host)
# print("Waiting for incoming connection...")
# conn, addr = s.accept()
# print(addr, "Connected")
#
# filename = input(str("Enter filename:"))
# file = open(filename, 'rb')
# file_data = file.read(1024)
# conn.send(file_data)
# print("Data has been transmitted...")













# STITCH IMAGE BACK TOGETHER
# Normally this will be in another location to stitch it back together
#read_file = open('chunkfile.txt', 'rb')

# Create the jpg file
#with open('images/stitched_together.jpg', 'wb') as image:
    #for f in read_file:
        #image.write(f)