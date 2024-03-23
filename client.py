
#crear un client en python
import argparse
import socket
import sys

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

def main():
    #parse arguments
    read_config_files()
    #setup client
    

if __name__ == '__main__':
    main()


def read_config_files(): 
        global debug_mode 
        parser = argparse.ArgumentParser()
        parser.add_argument("-d", "--debug", help="Enable debug mode", action="store_true")
        parser.add_argument("-f", "--file", help="Path to config file")
        args = parser.parse_args()   
        #activar el mode debug   
        if args.debug:     
             debug_mode = True   
        if args.file:    
             return args.file   
        else:     return None


def service_loop():
     print("iniciando el service loop")
     while True:
          state = NOT_REGISTERED
          new_register = 0
          register_loop()
          listen_loop()

# fase de registre
def register_loop():
    print("iniciando el register loop")
    #mentres el estat no sigui SEND_ALIVE
    """while (state != SEND_ALIVE) {
    // Function returning 0 -> No response from the server or wrong response
    if (register_process_active) { // Checks whether the client should start a new register process or continue with the previous
      // Make a register process
      if (register_process() == 0) continue;
    } else {
      // Continue with the previous register
      if (register_petition() == 0) {
        register_process_active = 1;
        continue;
      }
    }
    // Checks whether the server's register response is good or bad according to the protocol
    if (register_ack() == 0) continue;
    // Sends the client's information to the server, waits and checks if the given response from the server is correct according to the protocol
    register_info();
    if (state != REGISTERED) continue;
    // Sends the first ALIVE paquet to the server
    send_alive();
  }"""
        

def register_process():
    print("iniciando el register process")
    #si hem superat el nombre de procesos de registre
    #finalitzarem el registre
    if(reg_petition_iteration == reg_petition_max)
        exit(0)
        print("finalitzant el registre per superar el nombre de registres")
    #si no hem superat el nombre de procesos de registre
    #actualitzarem l'estat
    update_state(NOT_REGISTERED)
    #iniciem el registre
    register_iteration = 0

    return register_petition()

def register_petition():
     # enviar SUBS_REQ en un bucle fins que el servidor respongui
     