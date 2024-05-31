import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# target_address = "192.168.1.25"
target_address = "127.0.0.1"
port_no = 8080
sender_address = (target_address,port_no)
filename = "hello.txt"
file_read_status = False
with open(filename,"r") as file:
    while True:
        if not file_read_status:
            stack_read_text = filename
            file_read_status = True
        else:
            stack_read_text = file.read(1024)
            if stack_read_text == "":
                file_read_status = False
                file.close()
                break
        message = stack_read_text.encode("ascii")
        s.sendto(message,sender_address)
        
    

