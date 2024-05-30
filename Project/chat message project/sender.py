import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
target_address = "192.168.1.25"
# target_address = "127.0.0.1"
port_no = 2525
sender_address = (target_address,port_no)
quiet = True
while quiet:
    message = input("plz enter your message :")
    message_enc = message.encode("ascii")
    res = s.sendto(message_enc,sender_address)
    user_input = input("do you want to quiet it press Y/n :")
    if user_input =="Y"or user_input =="y":
        quiet = False
