import re

port = input('请输入一个端口:')
def is_port(port,paragraph):
	match = re.match(r'\S+',paragraph)
	return match.group() == port

def port_address(paragraph):
	result = re.search(r', address is (.+)\n',paragraph)
	return result.group(1)
with open('1.txt','r') as file_obj:
	while True:
		paragraph = ''
		while True:
			line = file_obj.readline()
			if not line:
				break
			if line =='\n':
				break
			paragraph += line
		if not paragraph:
			break
		if is_port(port,paragraph):
			print(port_address(paragraph))
			break

# print(is_port('I1','I1 is down'))
# print(port_address('tasdajshdjash, address is 10f3.116c\n'))


