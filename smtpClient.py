from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv_start = clientSocket.recv(1024).decode()

    helloCommand = 'HELO Alice\r\n'
    clientSocket.send(helloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    mailFrom = 'MAIL FROM:<alice@gmail.com\r\n'
    clientSocket.send(mailFrom.encode())
    recv_mailFrom = clientSocket.recv(1024).decode()

    rcpt = 'RCPT TO:<bob@gmail.com>\r\n'
    clientSocket.send(rcpt.encode())
    recv_rcpt = clientSocket.recv(1024).decode()

    data = 'DATA\r\n'
    clientSocket.send(data.encode())
    recv_data = clientSocket.recv(1024).decode()

    clientSocket.send(msg.encode())

    clientSocket.send(endmsg.encode())
    recv_sendMessage = clientSocket.recv(1024).decode()

    quit = 'QUIT\r\n'
    clientSocket.send(quit.encode())
    recv_quit = clientSocket.recv(1024).decode()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
