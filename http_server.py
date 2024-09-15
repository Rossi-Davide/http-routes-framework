#http server created from scratch
#built on top of level 4 sever components built in python the 
import socketserver
import os


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
            





        
            resource_name = type_request_descriptors[1].removeprefix('/')




            file = open(resource_name, 'r')

            encoded_file = file.encode('utf-8')








            response = "HTTP/1.1 200 OK\r\nCache-Control: no-cache, private\r\nContent-Length: 107\r\nDate: Mon, 24 Nov 2014 10:21:21 GMT\r\n\r\n<html><head><title></title></head><body>TIME : 1416824843 <br>DATE: Mon Nov 24 15:57:23 2014 </body></html>"

            response_encoded = response.encode('utf-8')

            self.request.sendall(response_encoded)


        except (Exception,OSError) as e:
            self.error_response(e)
            




        

        










server_address = ('127.0.0.1', 8000)

with socketserver.TCPServer(server_address,RequestHandlerOne) as server:

    print("Serving on port 8000")

    server.serve_forever()