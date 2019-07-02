from person_rls_record import Person
rows = Person().findAll()
outString = ""
outString +=("<html><head><title>People</title></head><body><table><tbody><tr><th>primary_key</th><th>first_name</th><th>last_name</th></tr>")
for row in rows:
     outString +=("<tr><td>")
     outString +=(str(row['primary_key']) )
     outString +=("</td><td>")
     outString +=(str(row['first_name']) )
     outString +=("</td><td>")
     outString +=(str(row['last_name']) )
     outString +=("</td></tr>")
outString +=("</tbody></table></body></html>")



