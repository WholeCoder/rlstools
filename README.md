# rlstools

Rlstools are a set of python scripts that are intended to mimic the way Ruby on Rails works.  Currently these tools only work on Linux because of the rls.sh bash driver script.  Ruby on Rails is a website development framework that allows a developer to create a CRUD applcaiton very quickly with scaffolding.  The aim of this project is to duplicate the functionality of Ruby on Rails and possibly enhance it.

In order to run these scripts you need to add these to your .bashrc file: 

**export RLSPATH=rlstools direcotry**
and

**export PATH=$RLSPATH:$PATH**
and

**export PYTHONPATH=rlstools directory**

You will also need to install the yaml plugin:

**pip3 install pyyaml**


# How to use rls tools

**```rls.sh new mynewwebapp```**  # create a new website

**```cd mynewwebapp```** # change to you new website's direcotry then:

**```rls.sh scaffold City address:string city:string zip_code:string```**

then run the migration tool:

**```migration_tool upgrade```**

then run serve so you can see your new website:

**```rls.sh serve```**

your new website is at **http://localhost:8080/City/get_form**

