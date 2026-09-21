from socket import *

msg = "\r\nI love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server
mailserver = 'list.winthrop.edu'

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))

recv = clientSocket.recv(1024).decode()
print(recv)

if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())

recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
mailFrom = 'MAIL FROM:<your_email@winthrop.edu>\r\n'
clientSocket.send(mailFrom.encode())

recv2 = clientSocket.recv(1024).decode()
print(recv2)

if recv2[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptTo = 'RCPT TO:<recipient_email@example.com>\r\n'
clientSocket.send(rcptTo.encode())

recv3 = clientSocket.recv(1024).decode()
print(recv3)

if recv3[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())

recv4 = clientSocket.recv(1024).decode()
print(recv4)

if recv4[:3] != '354':
    print('354 reply not received from server.')

# Send message data.
subject = 'Subject: SMTP Lab\r\n'
body = 'This is a test email sent using my own SMTP client.\r\n'

clientSocket.send((subject + body).encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())

recv5 = clientSocket.recv(1024).decode()
print(recv5)

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())

recv6 = clientSocket.recv(1024).decode()
print(recv6)

clientSocket.close()
