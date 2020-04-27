import socket
import time
import json
import os
user_name = input('enter username:')
def writetojson(filename, data):
        with open(filename, 'w') as fp:                                    #open file
                json.dump(data, fp)                                        #encoded string writing on file


def getfromjson():
        with open('file.json', 'r') as f:
                data = json.load(f)                    #convert json file to object
        converted_data = json.dumps(data)              #convert object to string
        return converted_data


filename = 'file.json'
data = {}
data['name'] = user_name

PORT = 5000                                                                #data will be send to this port number
HOST = "192.168.1.255"                                                     #AF_INET indicate ip adress is typr ipv4
announcer_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        #SOCK_DGRAM indicate connectoin type is UDP
announcer_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)     #to get permission to broadcast local network

while 1:
        path = ('/Users/ibr.sahin/PycharmProjects/P2P/filedirectory')      
        array_of_filenames = os.listdir(path)
        data['files'] = array_of_filenames
        writetojson(filename, data)
        mydata = getfromjson()
        announcer_socket.sendto(mydata.encode(), (HOST, PORT))
        print ("sent ")
        time.sleep(10)          #send UDP messages once per minute


















