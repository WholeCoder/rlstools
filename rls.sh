#!/bin/bash

create_directory() {
	
	if [ ! -d "$1" ]; then
		echo "Creating $1 directory."
		mkdir "$1"
	else
		echo "$1 directory already exists.  Not creating"
	fi
}

delete_directory_contents_safely() {
	[[ -d "$1" ]] && cd "$1" && rm *
}

if [ $# -lt 2 ]
then
	echo Not enough paramegers
	echo Usage:
	echo 	./rls.sh new new-app-name
	echo		OR
	echo	./rls.sh scaffold new-app-name/ attribute:datatype  attribute2:datatype
	exit 1
fi

if [ $1 = 'serve' ]; then
	./server.py
elif [ $1 = 'scaffold' ]; then
	appDirectory="$2"
	scaffoldName="$3"
	shift
	shift
	shift
	argsArray=("$@")
	argumentString=""
	for arg in "${argsArray[@]}"; do
		argumentString="$arg,$argumentString"
	done
	echo "Argument String is:  $argumentString"

	echo "Creating Scaffold"
	cd "$appDirectory"
	create_directory "controllers"
	cd controllers
	wDirectory=$PWD
	"../../write_controller_template.py" "$wDirectory" "$scaffoldName"
	cat "$wDirectory/$scaffoldName.py"
	cd ..
	create_directory "views"
	cd views
	wDirectory=$PWD
	"../../write_view_template.py" "$wDirectory" "$scaffoldName" "a:b"
	cat "$wDirectory/$scaffoldName.html"
	cd ..
	create_directory "models"
	cd models
	wDirectory=$PWD
	"../../write_model_template.py" "$wDirectory" "$scaffoldName" "$@"
	cat "$wDirectory/$scaffoldName.py"
	#append to the migration script

elif [ $1 == 'new' ]; then
	if [ ! -d $2 ]; then
		echo "Creating the app"
		mkdir $2
		cd $2
		touch config.yml
	else
		echo "App direcotry already exists"
	fi
fi


#
#while [[ $# -gt 0 ]]; do
#	echo "Argument $count = $1"
#	count=$((count + 1))
#	shift
#done
