import socket
import ssl
import json
import time
target_host = 'api.github.com'
target_port = 443
nome = input('Insira um Nome ')
repositorio = input('Insira um Repositorio ')
b_nome = bytes(nome, encoding='utf-8')
b_repositorio = bytes(repositorio, encoding='utf-8')
request = b"GET /repos/" + b_nome + b"/" + b_repositorio + b" "
request += b"HTTP/1.1\r\n"
request += b"Host: api.github.com\r\n"
request += b"User-Agent: Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36\r\n"
request += b"Accept: text/html,application/xhtml+xml+json,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3\r\n"
request += b'Accept: application/vnd.github+json\r\n'
request += b'Cookie: _octo=GH1.1.1700653853.1566866911; logged_in=yes; dotcom_user=salanho; _ga=GA1.2.656982550.1568050694; _gid=GA1.2.1543509806.1568050694\r\n\r\n'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

client.settimeout(5)

ssocket = ssl.wrap_socket(client, server_side=False, ssl_version=ssl.PROTOCOL_TLS)
ssocket.connect((target_host,target_port))  

ssocket.sendall(request)  

#header = ssocket.recv(898)
str_json = ''
while True:
    try:
       str_json += ssocket.recv().decode('utf-8') 
    except socket.timeout:
        break
#print(header)
#print('\n')
#print(str_json)
lista = str_json.split('\r\n\r\n')
print(lista[1])
ssocket.close()
client.close()