from rubsapp.models.Office import Office

print("Running template_Output")

rows = Office().findAll()
print("rows == "+str(rows))

currString = ""
currString +="<html><head><title>OfficeList</title></head><body><table><tbody><tr><th>zip_code</th><th>city</th><th>address</th></tr>"
for row in rows:
     currString +="<tr><td>"
     currString +=str(row['zip_code']) 
     currString +="</td><td>"
     currString +=str(row['city']) 
     currString +="</td><td>"
     currString +=str(row['address']) 
     currString +="</td></tr>"
currString +="</tbody></table></body></html>"



