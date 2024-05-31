import socket as sk
s = sk.socket(sk.AF_INET,sk.SOCK_DGRAM) #tcp
# ip_address = "192.168.1.34"
ip_address ="127.0.0.1"
port_no = 8080
my_address = (ip_address,port_no)
s.bind(my_address)
file_read_status = False

if not file_read_status:
    file_data = s.recvfrom(1024)
    filename = file_data[0].decode("ascii")
    print("file name is :" ,filename)
    file_read_status = True 
with open("n_"+filename,'w') as file1:
    while True:
         data = s.recvfrom(1024)
         message = data[0].decode("ascii")      
         file1.write(message)
         file1.flush()
         print(message)
         if message =="":
             file_read_status = False
             file1.close()
             break