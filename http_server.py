#http server created from scratch
#built on top of level 4 sever components built in python the 
import socketserver
import sys


prova_obj = None


class RequestHandlerOne(socketserver.BaseRequestHandler):

    def error_response(self,exception = None):

        print(exception)

        ex_encoded = str(exception).encode('utf-8')

        self.request.sendall(ex_encoded)



    def handle(self):

        try:
        
            msg,ancdata,flags,addr = self.request.recvmsg(4096)





            #decoding the incoming request

            str_msg = msg.decode('utf-8')

            self.data = str_msg.split('\r\n')

            #exctracting name of the requested resource
            type_request_descriptors = self.data[0].split(' ')

            if type_request_descriptors[0] != 'GET' :

                raise Exception("Errore, solo get richieste processabili")
            


            response = "HTTP/1.1 200 OK\r\nCache-Control: no-cache, private\r\nDate: Mon, 24 Nov 2014 10:21:21 GMT\r\n\r\n"
            response_encoded = response.encode('utf-8')
            

            self.request.sendall(response_encoded)

        
            resource_name = type_request_descriptors[1].removeprefix('/')


            with open(resource_name, 'rb') as file:

                while buffer := file.read(4096):

                    
                    self.request.sendall(buffer)


                



        except (Exception,OSError) as e:
            self.error_response(e)
            




        

        










server_address = ('127.0.0.1', 8000)

with socketserver.TCPServer(server_address,RequestHandlerOne) as server:

    print("Serving on port 8000")

    server.serve_forever()