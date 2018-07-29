# jim-messenger
JSON instant messenger with presence control and AES encryption.

How to start:

1. Run server:
		- with default parameters in command line:
								python3.6 server.py
		- with host and port specified:
								python3.6 server.py -a 192.168.0.6 -p 9999

2. Run any number (max 5) of clients:
		- console clients with default parameters:
								python3.6 clnt_cli.py
		- console clients with specified parameters:
								python3.6 clnt_cli.py -a 192.168.0.7 -p 9999
		- gui clients at the same way:
								python3.6 clnt_gui.py

P.S. Use PyCharm to avoid module not found issue with pycryptodome.

Thx a lot to Leo Orlov and GeekBrains.
Ilia Kruglov, 29072018.
