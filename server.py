#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler,HTTPServer
from person_rls_record import Person
#from master_template import headString
import importlib
from template_parser import TemplateParser
import os
import cgi
from sqlite_adapter import SqliteDatabaseAdapter
import re

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Cache-Control', 'no-cache')
        self.end_headers()
        
	# Send the html message
        #self.wfile.write("test".encode())
        print (self.path.split("/"))
        entity = self.path.split("/")[1]
        print("entity 2 == "+entity)
        template_file = entity
        actiono = ""
        if len(self.path.split("/")) == 3:
            action = self.path.split("/")[2]
        else:
            action = "index"
        entity = self.path.split("/")[1]

        outputString = '' 
#        if not ".get" in entity:
#            outputString += "from rubsapp.models."+entity+" import "+entity+"\n\n"
#            outputString += "print(\"Running template_Output\")\n\n"

#            outputString += "rows = "+entity+"().findAll()\n"
#            outputString += "print(\"rows == \"+str(rows))\n\n"
        

        print("entity == "+entity)
        print("action == "+action)

        TemplateParser(entity,action)
        #importlib.invalidate_caches()
        mdle = importlib.import_module('template_output')
        mdle = importlib.reload(mdle)
        print("mdle == "+mdle.currString)
        #mdle = importlib.import_module('out')#outString = eval("out.py")
        self.wfile.write(mdle.currString.encode())
        return

    def send_headers(self, status, content_type, value):
        self.send_response(status)
        self.send_header(content_type, value)
        self.end_headers()

    def do_POST(self):
        #self.send_response(200)
        
        
	# Send the html message
        #self.wfile.write("test".encode())
        entity = self.path[:]
        print("entity == "+entity)
        #self.wfile.write(entity.encode())
        #self.send_response(302)
        #self.send_header('Location', '/'+entity)
        self.send_headers(302, 'Location', 'http://localhost:8080'+entity) 
        #self.wfile.write("<script type=\"text/javascript\">alert(\"works\"</script>" .encode())
        print( "incomming http: ", self.path )

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'})
        dct = {}
        for i in form.keys():
            dct[i] = form[i].value
            if "'" in dct[i]:
                dct[i] = dct[i].replace("'", "''")

        print ("dictionary == " +str(dct))
        SqliteDatabaseAdapter.getInstance().createNewRecord(entity[1:],dct)
        #ent().create(dct)

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print ('Started httpserver on port ' , PORT_NUMBER)
	
    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print ('^C received, shutting down the web server')
    server.socket.close()
	
