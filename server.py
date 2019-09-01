#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import importlib
from template_parser import TemplateParser
import cgi
from sqlite_adapter import SqliteDatabaseAdapter
from os import curdir
import os
import logging
from collections import OrderedDict

logging.basicConfig(level=logging.INFO, format=' %(asctime)s -- %(message)s')

#  This will disable debug logging in every file.
logging.disable(logging.DEBUG)

logging.debug('Start of program')

PORT_NUMBER = 8080

# This class will handles any incoming request from
# the browser


class myHandler(BaseHTTPRequestHandler):
    # Handler for the GET requests
    def do_GET(self):
        if self.path.endswith(".ico"):
            return

        sendReply = False
        if self.path.endswith(".js"):
            mimetype = 'application/javascript'
            sendReply = True
        if self.path.endswith(".css"):
            mimetype = 'text/css'
            sendReply = True

        if sendReply:
            # Open the static file requested and send it
            f = open(os.path.join(curdir, self.path))
            self.send_response(200)
            self.send_header('Content-type', mimetype)
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
            return

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Cache-Control', 'no-cache')
        self.end_headers()

        # Send the html message
        # self.wfile.write("test".encode())
        logging.debug(self.path.split("/"))
        entity = self.path.split("/")[1]
        logging.debug("entity 2 == "+entity)
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
        logging.debug("entity == "+entity)
        logging.debug("action == "+action)

        TemplateParser(entity, action)
        mdle = importlib.import_module('template_output')
        mdle = importlib.reload(mdle)
        logging.debug("mdle == "+mdle.currString)
        self.wfile.write(mdle.currString.encode())
        return

    def send_headers(self, status, content_type, value):
        self.send_response(status)
        self.send_header(content_type, value)
        self.end_headers()

    def do_POST(self):
        entity = self.path[:]
        logging.debug("entity == "+entity)
        self.send_headers(302, 'Location', 'http://localhost:8080'+entity)
        logging.debug("incomming http: ", self.path)

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'})
        dct = OrderedDict()
        for i in form.keys():
            dct[i] = form[i].value

        SqliteDatabaseAdapter.getInstance().createNewRecord(entity[1:], dct)


try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    logging.debug('Started httpserver on port %s', PORT_NUMBER)

    # Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    logging.debug('^C received, shutting down the web server')
    server.socket.close()
