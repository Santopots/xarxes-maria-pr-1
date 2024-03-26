
#crear un client en python
import argparse
import configparser
import socket
import sys

#classe que representi la informació del client
class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

def main():
    #parse arguments
    set()
    #setup client
    
    

if __name__ == '__main__':
    main()

def set(): 
  global debug_mode
  parser = argparse.ArgumentParser()
  parser.add_argument("-d", "--debug", help="Enable debug mode", action="store_true")
  parser.add_argument("-c", metavar="filename", default="client.cfg", nargs='?', const="client.cfg", help="Especifica el fitxer de configuració.")
  args = parser.parse_args()   
  #activar el mode debug   
  debug_mode = args.debug

  read_config_file(args.c)

def read_config_file(filename):
    global Name, Situation, Elements, MAC, Local_TCP, Server, Srv_UDP

    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        key, value = line.strip().split(' = ')
        if key == 'Name':
            Name = value
            print(Name)
        elif key == 'Situation':
            Situation = value
            print(Situation)
        elif key == 'Elements':
            Elements = value
            print(Elements)
        elif key == 'MAC':
            MAC = value
            print(MAC)
        elif key == 'Local-TCP':
            Local_TCP = int(value)
            print(Local_TCP)
        elif key == 'Server':
            Server = value
            print(Server)
        elif key == 'Srv-UDP':
            Srv_UDP = int(value)
            print(Srv_UDP)

