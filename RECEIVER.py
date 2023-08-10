import socket

def start_receiver():
    receiver_host = socket.gethostname()
    receiver_port = 5050
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((receiver_host, receiver_port))
    details = client_socket.recv(1024).decode()
    print(details)
    
    adv_win_size = int(input("Enter the advertisement window size: "))
    client_socket.send(str(adv_win_size).encode())
    
    pkt_ack = 0
    while True:
        print("Press 1 to ACKNOWLEDGE packets")
        print("Press 2 to DROP packets")
        choice = int(input("Choice: "))
        
        if choice == 1:
            if pkt_ack == 0:
                pkt_ack = 1
            ack = 'acknowledged'
            print("The Number of Packets Acknowledged: ", pkt_ack)
            print("")
            pkt_ack *= 2
            client_socket.send(ack.encode())
            continue
        elif choice == 2:
            ack = 'drop'
            client_socket.send(ack.encode())
            break
        else:
            break
    
    print("Connection is closed")
    client_socket.close()

if __name__ == '__main__':
    start_receiver()
