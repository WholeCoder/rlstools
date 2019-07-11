from rubsapp.models.Person import Person

print("Running template_Output")

rows = Person().findAll()
print("rows == "+str(rows))

currString = ""
currString +="<html><head><title>Ruben'sPeople</title></head><body><table><tbody><tr><th>last_name</th><th>first_name</th></tr>"
for row in rows:
     currString +="<tr><td>"
     currString +=str(row['last_name']) 
     currString +="</td><td>"
     currString +=str(row['first_name']) 
     currString +="</td></tr>"
currString +="</tbody></table></body></html>"



