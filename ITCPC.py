import socket
import sys

if len(sys.argv) >= 3:
    ip, port = sys.argv[1], int(sys.argv[2])
    while True:
        try:
            input_data = input('> ')
            if input_data == None:
                continue
            send_data = eval('\'' + input_data + '\'')
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                s.send(send_data.encode('utf-8'))
                recv_data = s.recv(4096).decode('utf-8')
                print(recv_data)
                s.close()
            except ConnectionRefusedError:
                print(f'Couldnt connect to {ip}:{port}')
        except KeyboardInterrupt:
            print(f'\nClosing connection with {ip}:{port}')
            s.close()
            print('Connection closed. Exiting')
            exit()
else:
    print('Invalid Syntax')
    print('Syntax: python3 ITCPC.py ip port')
    print('Example: python3 ITCPC.py 127.0.0.1 80')
