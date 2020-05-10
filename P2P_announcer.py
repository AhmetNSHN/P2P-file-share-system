import socket
import time
import json
import os
user_name = input('enter username:')
def writetojson(filename, data):
        with open(filename, 'w') as fp:
                json.dump(data, fp)


def getfromjson():
        with open('file.json', 'r') as f:
                data = json.load(f)
        converted_data = json.dumps(data)
        return converted_data


filename = 'file.json'
data = {}
data['name'] = user_name

PORT = 5000
HOST = "25.255.255.255"
announcer_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
announcer_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while 1:
        path = ('filedirectory')
        array_of_filenames = os.listdir(path)
        data['files'] = array_of_filenames
        writetojson(filename, data)
        mydata = getfromjson()
        announcer_socket.sendto(mydata.encode(), (HOST, PORT))
        print("sent ")
        time.sleep(10)
