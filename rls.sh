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

if [ $# -lt 1 ]
then
	echo Not enough paramegers
	echo Usage:
	echo 	rls.sh new new-app-name
	echo		OR
	echo	rls.sh scaffold EntityName attribute:datatype  attribute2:datatype
	echo          OR
	echo	rls.sh serve
    echo         OR
    echo	rls.sh model Entityname attribut:datatype attribut2:datatype
	exit 2
fi

if [ $1 = 'serve' ]; then
	server.py
elif [ $1 = 'scaffold' ]; then
	appDirectory="."
	scaffoldName="$2"
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
	"write_controller_template.py" "$wDirectory" "$scaffoldName"
	cat "$wDirectory/$scaffoldName.py"
	cd ..
	create_directory "models"
	cd models
	wDirectory=$PWD
	"write_model_template.py" "$wDirectory" "$scaffoldName"
	#cat "$wDirectory/$scaffoldName.migration"
	cd ..
	create_directory "migrations"
	#cd migrations
	wDirectory=$PWD
	"generate_migration.py" "$wDirectory" "$scaffoldName" "$@"
	#new_version_for_next_migration=`python3 print_out_next_database_version_number.py`
	#"../../migration_tool.py" "upgrade" "$wDirectory" "$scaffoldName" "$new_version_for_next_migration"
	#cd ..
	create_directory "views"
	cd views
	wDirectory=$PWD
	"master_template.py" "$wDirectory" "$scaffoldName" "$@"

	#append to the migration script
	cd ../..

elif [ $1 == 'new' ]; then
	if [ ! -d $2 ]; then
		echo "Creating the app"
		mkdir $2
		cd $2
		touch config.yaml
        echo "config:" >> config.yaml
        echo "    database:  ./my_db.db" >> config.yaml
        echo "    database_adapter:  sqlite" >> config.yaml
    else
		echo "App directory already exists"
	fi
elif [ $1 == 'model' ]; then
	scaffoldName="$2"
	shift
	shift
    create_directory "models"
	cd models
	wDirectory=$PWD
	"write_model_template.py" "$wDirectory" "$scaffoldName"
	#cat "$wDirectory/$scaffoldName.migration"
	cd ..
	create_directory "migrations"
	#cd migrations
	wDirectory=$PWD
	"generate_migration.py" "$wDirectory" "$scaffoldName" "$@"
fi


#
#while [[ $# -gt 0 ]]; do
#	echo "Argument $count = $1"
#	count=$((count + 1))
#	shift
#done
