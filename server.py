#!/usr/bin/python
from http.server import BaseHTTPRequestHandler,HTTPServer
from person_rls_record import Person

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
	# Send the html message
        rows = Person().findAll()
        rString = "<html><head><title>Ruben's People</title></head><body><table>"
        rString += "<tr>"
        for key in rows[0].keys():
            rString += "<th>" + key + "</th>"
        rString += "</tr>"

        for row in rows:
            rString += "<tr>"
            for key in rows[0].keys():
                rString += "<td>" + str(row[key]) + "</td>"
            rString += "</tr>"
        rString += "</table></body></html>"
    
        self.wfile.write(rString.encode())
        return

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
	
