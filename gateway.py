import socket
import sys


BIND_TCP_HOST = socket.gethostname()
BIND_TCP_SOCKET = 2021
TCP_PKG_SIZE = 4092



def proceso_datos(data):
    return 'RESPUESTA: ' + str(data, encoding='utf-8')


if __name__ == '__main__':
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')
    # bind the socket to a public host, and a well-known port
    server_address = ((socket.gethostname(), BIND_TCP_SOCKET))
    
    try:
        a = sock.bind(server_address)
    except:
        print('Socket not binded... Now exiting')
        sys.exit(0)
    
    # become a server socket
    sock.listen(5)
    print('Socket bind at  %s: %04u' % (server_address))

    while True:
        connection, client_address = sock.accept()
        try:
            print(f'connection from {client_address}')

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(TCP_PKG_SIZE)
                print('received "%s"' % data)
                if data:
                    print('sending data back to the client')
                    # PROCESAR DATOS 
                    data = proceso_datos(data)
                    connection.sendall(data.encode('utf-8'))
                else:
                    print(f'No more data from {client_address}')
                    break
                
        finally:
            # Clean up the connection
            connection.close()





