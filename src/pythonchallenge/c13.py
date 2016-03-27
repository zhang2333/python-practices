import xmlrpc.client

x = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print(x.phone('Bert'))
