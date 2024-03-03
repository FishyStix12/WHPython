# White Hat Python
# By: Nicholas Fisher
# 
**The creator is not resposible for any damage caused by these programs because YOU AGREE TO THE CONSEQUENCES IF YOU RUN These SCRIPTS!!!!!** <br />

This is a repository of White hat python codes to be used for Pentesting. <br />

**The Following List gives a short description of all the scripts in this repository:** <br />
1. VenvConfig.sh - This script creates new python3 environments,loads one module, and tests to see if the enviroment is using python3. To ensure that this script works please install the venv tool. The command to install venv is in the description of this script. <br /> 
2. IDEConfig.sh - This script is used to install and setup the Visual Studio IDE. <br />
3. TCPClient.py - This script is used to help Pentesters to whip up a TCP client. The user inputs an IPv4 address or hostname and TCP port to establish the client connection. <br />
4. UDPClient.py - This script is used to help Pentesters to whip up a UDP client. The user inputs an IPv4 address or hostname and UDP Port to establish the client connection. Runs on Python 3. <br />
5. TCPServer.py - This script is used to help Pentesters to whip up a Threaded TCP Server on python 3. Please provide an IPv4 Address or hostname and the appropriate TCP port for this script to work. <br />
6. netcat.py - A Python implementation of the NetCat tool, offering file transfer, command execution, and interactive command shell functionalities over TCP/IP connections. This tool provides <br />
   a flexible command-line interface for both client and server modes, allowing for easy network operations and troubleshooting. <br />
7. proxy.py - This script implements a basic TCP proxy. It listens on a specified local host and port, forwards incoming connections to a remote host and port, and relays data between the client and the remote server. It can be used for various purposes such as debugging, monitoring, or modifying network traffic. <br />
8. ssh_cmd.py - This script allows the user to execute a command on a remote server over SSH. It prompts the user for their username, password, server IP, port, and command. If no input is provided for the IP, port, or command, default values are used. <br />

**Example outputs of some of the scripts!** <br />
1. TCPServer.py output: <br />
[*] Listening on 0.0.0.0:9998 <br />
[*] Accepted Connection from 127.0.0.1:49704 <br />
[*] Received: GET / HTTP/1.1 <br />
Host: google.com <br />
2. proxy.py output: <br />
   ./proxy.py 127.0.0.1 9000 10.21.132.1 9000 True <br />
3. ssh_cmd.py output: <br />
    Username: user <br />
    Password: <br />
    Enter Server IP: 192.168.1.203 <br />
    Enter port or <CR>: 2222 <br />
    Enter command or <CR>: id <br />
    --- Output --- <br />
   uid=0(root) gid=0(root) groups=0(root) <br />
