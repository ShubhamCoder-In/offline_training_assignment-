import socket as sk
s = sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
ip_address = "192.168.1.34"
# ip_address ="127.0.0.1"
port_no = 2525
my_address = (ip_address,port_no)
s.bind(my_address)
while True:
    data = s.recvfrom(100)
    message = data[0]
    ip_tuple = data[1]
    sender_ip = ip_tuple[1]
    sender_port = ip_tuple[0]
    meassage = message.decode("ascii")
    with open(str(sender_ip)+".txt","a+") as file:
        file.write(meassage+"\n")
    print(message)