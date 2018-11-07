from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import socket 
host = socket.gethostname()

class HttpProcessor(BaseHTTPRequestHandler):
    
    def do_GET(self):
        global host
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write("Allow, this is       " + host)

serv = HTTPServer(("0.0.0.0",8080),HttpProcessor)
serv.serve_forever()

