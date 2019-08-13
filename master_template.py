#!/usr/bin/python3
import sys


class Template:
    def __init__(self):
        pass

    def generateTemplate(self):

        parameter_list = []
        count = 3
        while count < len(sys.argv):
            parameter_list.append(sys.argv[count].split(":")[0])
            count += 1
        print("parameter_list == " + str(parameter_list))

        headString = '''
<html>
	<head>
		<title>''' # noqa
        headString += sys.argv[2] + " List" # noqa
        headString += '''</title>
        <meta charset="utf-8">
        <script defer src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<script defer src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>

<script defer src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>

<link href="https://fonts.googleapis.com/css?family=Roboto+Mono" rel="stylesheet">

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">
        
        </head>
	<body>

<header>
      <div class="collapse bg-dark" id="navbarHeader">
        <div class="container">
          <div class="row">
            <div class="col-sm-8 col-md-7 py-4">
              <h4 class="text-white">About</h4>
              <p class="text-muted">Add some information about the album below, the author, or any other background context. Make it a few sentences long so folks can pick up some informative tidbits. Then, link them off to some social networking sites or contact information.</p>
            </div>
            <div class="col-sm-4 offset-md-1 py-4">
              <h4 class="text-white">Contact</h4>
              <ul class="list-unstyled">
                <li><a href="#" class="text-white">Follow on Twitter</a></li>
                <li><a href="#" class="text-white">Like on Facebook</a></li>
                <li><a href="#" class="text-white">Email me</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="navbar navbar-dark bg-dark shadow-sm">
        <div class="container d-flex justify-content-between">
          <a href="#" class="navbar-brand d-flex align-items-center">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mr-2"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>
            <strong>Album</strong>
          </a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarHeader" aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
        </div>
      </div>
    </header>



		<table>
			<tbody>
				<tr>''' # noqa

        print("second parameter_list"+str(parameter_list))# noqa
        count = 0
        while count < len(parameter_list):
            headString += "<th>" + parameter_list[count] + "</th>"
            count += 1

        headString += '				</tr>'
        headString += "<% for row in rows: %>"
        headString += '<tr>'
        count = 0
        while count < len(parameter_list):
            headString += "<td><%= html.escape(str(row[\""+parameter_list[count]+"\"])) %></td>"# noqa
            count += 1
        headString += '</tr>'
        headString += "<% end-for %>"
        headString += '''
                        </tbody>
		</table>

<footer class="container">
        <p class="float-right"><a href="#">Back to top</a></p>
        <p>© 2017-2018 Company, Inc. · <a href="#">Privacy</a> · <a href="#">Terms</a></p>
      </footer>

	</body>
</html>
'''# noqa

        print(headString)# noqa
        with open(sys.argv[1]+"/"+sys.argv[2]+".pyht", 'w') as file_handle:
            file_handle.write(headString)
#########

    def generateFormTemplate(self):

        parameter_list = []
        count = 3
        while count < len(sys.argv):
            parameter_list.append(sys.argv[count].split(":")[0])
            count += 1
        print("parameter_list == " + str(parameter_list))

        headString = '''
<html>
	<head>
		<title>''' # noqa
        headString += sys.argv[2] + " Form" # noqa
        headString += '''</title>
	<meta charset="utf-8">
        <script defer src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<script defer src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>

<script defer src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>

<link href="https://fonts.googleapis.com/css?family=Roboto+Mono" rel="stylesheet">

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">
        
        </head>
	<body>

<header>
      <div class="collapse bg-dark" id="navbarHeader">
        <div class="container">
          <div class="row">
            <div class="col-sm-8 col-md-7 py-4">
              <h4 class="text-white">About</h4>
              <p class="text-muted">Add some information about the album below, the author, or any other background context. Make it a few sentences long so folks can pick up some informative tidbits. Then, link them off to some social networking sites or contact information.</p>
            </div>
            <div class="col-sm-4 offset-md-1 py-4">
              <h4 class="text-white">Contact</h4>
              <ul class="list-unstyled">
                <li><a href="#" class="text-white">Follow on Twitter</a></li>
                <li><a href="#" class="text-white">Like on Facebook</a></li>
                <li><a href="#" class="text-white">Email me</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="navbar navbar-dark bg-dark shadow-sm">
        <div class="container d-flex justify-content-between">
          <a href="#" class="navbar-brand d-flex align-items-center">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mr-2"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>
            <strong>Album</strong>
          </a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarHeader" aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
        </div>
      </div>
    </header>

		<table>
			<tbody>''' # noqa
        headString += "<form action=\"/"+sys.argv[2]+"\" method=\"post\">" # noqa
        print("second parameter_list"+str(parameter_list))
        count = 0
        while count < len(parameter_list):
            headString += "<tr>"
            headString += "<td>" + parameter_list[count] + "</td>"
            headString += "<td><input type=\"text\" name=\""+parameter_list[count]+"\"/></td>"# noqa
            headString += '</tr>'
            count += 1
        headString += "<tr><td colspan=2 ><button type=\"submit\">Save</button></td></tr>"# noqa
        headString += "</form></tbody></table>"
        headString += '''<footer class="container"><p class="float-right"><a href="#">Back to top</a></p><p>© 2017-2018 Company, Inc. · <a href="#">Privacy</a> · <a href="#">Terms</a></p></footer></body>'''  # noqa
        headString += "</html>"
        print(headString)
        with open(sys.argv[1]+"/"+sys.argv[2]+".get.pyht", 'w') as file_handle:
            file_handle.write(headString)


Template().generateTemplate()
Template().generateFormTemplate()
