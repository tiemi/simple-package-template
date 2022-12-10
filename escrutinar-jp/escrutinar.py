import socket
import requests



def sondarip(ip=None ,* ,mostrar_flag=False):
	
	whois = "https://ipwho.is/"
	
	if ip is None:
		requisicao = requests.get(whois).json()
	else:
		ip = ip.strip()
		requisicao = requests.get(f"{whois}{ip}").json()
	
	if not mostrar_flag:
		requisicao.pop('flag', None)
	
	return requisicao
	
	
	
def pediripsite(host):
	
	host = host.strip()
	host = host.replace('https://www.', '')
	host = host.replace('http://www.', '')
	host = host.replace('www.', '')
	
	ip = socket.gethostbyname(host)
	
	return ip
	
