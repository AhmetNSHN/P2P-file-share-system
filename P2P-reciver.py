import socket
import json

content_dictionary = { }


def writetojson(filename, data):
    with open(filename, 'w') as fp:  # open file
        json.dump(data, fp)

def mergeDict(dict1, dict2):
    ''' Merge dictionaries and keep values of common keys in list'''
    dict3 = {**dict1, **dict2}
    for key, value in dict3.items():
        if key in dict1 and key in dict2:
            if value in dict1 and value not in dict2:
                if [value, dict1[key]] not in dict3:
                    dict3[key] = [value, dict1[key]]

    return dict3

PORT = 5000
reciver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
reciver_socket.bind(("",PORT))
while 1:
    print ("reciving?")
    data, addr, = reciver_socket.recvfrom(1024)
    IP = addr[0]
    print(data)
    filesINnetwork = json.loads(data)
    formated_dictionary = {i: IP for i in filesINnetwork['files']}
    content_dictionary = mergeDict(formated_dictionary, content_dictionary)
    writetojson("content_dictionary.json", content_dictionary)










































