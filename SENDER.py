import socket

def start_sender():
    server_host = socket.gethostname()
    server_port = 5050
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(1)
    print("Waiting for connection {}:{}".format(server_host, server_port))
    client_socket, client_addr = server_socket.accept()
    print("Received connection from: ", client_addr)
    details = "ANANYA PILLAI 21BIT0081"
    print(" ")
    client_socket.send(details.encode())
    recv_win_size = int(client_socket.recv(1024).decode())
    print("Received Advertisement Window(AW) Size: ", recv_win_size)
    print(" ")
    
    congestion_win = 1
    congestion_th = 0
    pkt_sent = 0
    
    while True:
        if congestion_win < recv_win_size:
            for i in range(congestion_win):
                print("congestion window (CW):", congestion_win)
                print("Packets Sent: ", congestion_win)
                ack = client_socket.recv(1024).decode()
                
                if ack == 'acknowledged':
                    if pkt_sent == 0:
                        pkt_sent = 1
                    print("Packets Acknowledged: ", pkt_sent)
                    pkt_sent *= 2
                    congestion_win = congestion_win * 2
                    
                    if congestion_win >= recv_win_size:
                        server_socket.close()
                        client_socket.close()
                        break
                    continue
                elif ack == 'drop':
                    congestion_th = congestion_win // 2
                    congestion_win = 0
                    break
                
            if congestion_win == 0:
                congestion_win = 1
                print("Congestion Threshold: ", congestion_th)
                break
            else:
                continue
        else:
            print("Congestion window(CW) cannot exceed advertise window(AW)")
            break
    
    server_socket.close()

if __name__ == '__main__':
    start_sender()
