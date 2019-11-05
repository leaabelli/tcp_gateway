import socket
import sys

BIND_TCP_HOST = socket.gethostname()
BIND_TCP_SOCKET = 2021
TCP_PKG_SIZE = 4092

def proceso_datos(data):
    return 'OK'


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
        try:
            connection, client_address = sock.accept()
        except:
            connection.close()
            continue
        print(f'Open connection from [{client_address[0]}:{client_address[1]}]')
        while True:
            try:
                data = connection.recv(TCP_PKG_SIZE)
            except:
                break
            print(f'--> [{client_address[0]}:{client_address[1]}]\t({len(data)}): "{data}"')
            if data:
                # PROCESAR DATOS 
                data = proceso_datos(data)
                connection.sendall(data.encode('utf-8'))
                print(f'<-- [{client_address[0]}:{client_address[1]}]\t({len(data)}): "{data}"')
            else:
                break
        print(f'Close connection from [{client_address[0]}:{client_address[1]}]')
        connection.close()

