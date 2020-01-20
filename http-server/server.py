from http.server import BaseHTTPRequestHandler
import os
import cgi

from routes.main import routes

from response.staticHandler import StaticHandler
from response.templateHandler import TemplateHandler
from response.badRequestHandler import BadRequestHandler


class Server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return

    def do_GET(self):
        split_path = os.path.splitext(self.path)
        request_extension = split_path[1]

        if request_extension == "" or request_extension == ".html":
            if self.path in routes:
                handler = TemplateHandler()
                handler.find(routes[self.path])
            else:
                handler = BadRequestHandler()
        elif request_extension == ".py":
            handler = BadRequestHandler()
        else:
            handler = StaticHandler()
            handler.find(self.path)

        self.respond({
            'handler': handler
        })
    
    
    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                    'CONTENT_TYPE':self.headers['Content-Type'],
                    })
        
        # If I wanted not to overwrite files I would do the following
        # if os.path.exists(filename):
        #     self.send_response(409, 'Conflict')
        #     self.end_headers()
        #     reply_body = '"%s" already exists\n' % filename
        #     self.wfile.write(reply_body.encode('utf-8'))
        #     return

        textInput = form.getvalue('textInput')
        open('temp/textInput.txt', "wb").write(bytes(textInput, 'UTF-8'))

        singleFile = "temp/" + form['singleFileInput'].filename
        data = form['singleFileInput'].file.read()
        open(singleFile, "wb").write(data)

        multipleFiles = form['multipleFileInput']
        for f in multipleFiles:
            filePath = "temp/" + f.filename          
            open(filePath, "wb").write(f.file.read())        

        self.send_response(201)
        self.end_headers()        
        self.wfile.write(bytes("Saved".encode("UTF-8")))
                      

    def handle_http(self, handler):
        status_code = handler.getStatus()

        self.send_response(status_code)

        if status_code == 200:
            content = handler.getContents()
            self.send_header('Content-type', handler.getContentType())
        else:
            content = "404 Not Found"

        self.end_headers()

        return bytes(content, 'UTF-8')

    def respond(self, opts):
        response = self.handle_http(opts['handler'])
        self.wfile.write(response)
