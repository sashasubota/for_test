from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import socket 
import git
host = socket.gethostname()
repo = git.Repo("/home/subotaoleksandr/Http_test/")
commit = repo.commit('HEAD')

class HttpProcessor(BaseHTTPRequestHandler):
    
    def do_GET(self):
        global host
        global commit
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write("Allow, this is:" + host)
        self.wfile.write("<body><p>Commit hash:</p>"+str(commit))
        self.wfile.write("<body><p>This is a test.</p>")

serv = HTTPServer(("0.0.0.0",8080),HttpProcessor)
serv.serve_forever()
