from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from github import Github
import socket 

#import git - just for local repo
host = socket.gethostname()
#repo = git.Repo("github.com/sashasubota/for_test")
#commit = repo.commit('HEAD')
g = Github('6903782c3534e8ce6c2f459736fcafe25bccb0a9')
branch = g.get_repo("sashasubota/for_test").get_branch("master")
commit = branch.commit

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
