import socket
import json

content_dictionary = { }

PORT = 5000
reciver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
reciver_socket.bind(("",PORT))    #to tell socket to listen particular port for particular host
while 1:
    print ("reciving?")
    data, addr, = reciver_socket.recvfrom(1024)
    IP = addr[0]
    print(data)
    filesINnetwork = json.loads(data)                                      #convert binary string to dictionary
    content_dictionary = {i: IP for i in filesINnetwork['files']}          #file names converted to dictionary key and IP of their
    with open("content_dictionary.txt", 'w') as fp:  # open file           #owners is stored as their value
        json.dump(content_dictionary, fp)
                                                                            #contet dictionary.txt will be used by P2P-downloader








#for files in filesINnetwork: for(i = files; i < length of files; i++)


















