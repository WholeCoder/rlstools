#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import importlib
from template_parser import TemplateParser
import cgi
from sqlite_adapter import SqliteDatabaseAdapter

PORT_NUMBER = 8080

# This class will handles any incoming request from
# the browser


class myHandler(BaseHTTPRequestHandler):
    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Cache-Control', 'no-cache')
        self.end_headers()

        # Send the html message
        # self.wfile.write("test".encode())
        print(self.path.split("/"))
        entity = self.path.split("/")[1]
        print("entity 2 == "+entity)
        if len(self.path.split("/")) == 3:
            action = self.path.split("/")[2]
        else:
            action = "index"
        entity = self.path.split("/")[1]

#        if not ".get" in entity:
#            outputString += "from rubsapp.models."+entity+" import "+entity+"\n\n" # noqa
#            outputString += "print(\"Running template_Output\")\n\n"

#            outputString += "rows = "+entity+"().findAll()\n"
#            outputString += "print(\"rows == \"+str(rows))\n\n"
        print("entity == "+entity)
        print("action == "+action)

        TemplateParser(entity, action)
        mdle = importlib.import_module('template_output')
        mdle = importlib.reload(mdle)
        print("mdle == "+mdle.currString)
        self.wfile.write(mdle.currString.encode())
        return

    def send_headers(self, status, content_type, value):
        self.send_response(status)
        self.send_header(content_type, value)
        self.end_headers()

    def do_POST(self):
        entity = self.path[:]
        print("entity == "+entity)
        self.send_headers(302, 'Location', 'http://localhost:8080'+entity)
        print("incomming http: ", self.path)

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'})
        dct = {}
        for i in form.keys():
            dct[i] = form[i].value
            if "'" in dct[i]:
                dct[i] = dct[i].replace("'", "''")

        SqliteDatabaseAdapter.getInstance().createNewRecord(entity[1:], dct)


try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Started httpserver on port ', PORT_NUMBER)

    # Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
