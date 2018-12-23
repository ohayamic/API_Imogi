# API_Imogi

Common code for the Relational Databases and Full Stack Fundamentals courses
# Step 1
## Setting Up
Follow the instructions on installing Git, VirtualBox and Vagrant on your respective system.Some helpful links are listed below
* [Virtual Box](https://www.virtualbox.org/wiki/Linux_Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)

From the terminal run the following commands 
- Download the file using ```git clone http://github.com/<username>/API_Imogi_Site imogi```
- This will give you a directory named ```imogi``` that is a clone of your remote ```API_Imogi_Site ``` repository.
- Then ```cd imogi``` to enter into the directory just created
- Then run ```vangrant up```
- When **vagrant up** is ran, it installs all the libraries needed for the application to run

Once it is up and running, type ```vagrant ssh```. This will log your terminal into the virtual machine, and you'll get a Linux
shell prompt. When you want to log out, type ```exit``` at the shell prompt. To turn the virtual machine off (without deleting
anything), type ```vagrant halt.``` If you do this, you'll need to run ```vagrant up``` again before you can log into it.

## Running the App
Navigate to the ```imogi``` directory on your system and issue the following command
- Type ```python views.py``` and follow the instruction that is displayed on the command shell
- Type ```ctlr + c ``` to end the session

## Step 2 - Getting Familiar with project

Now that you have your server running, you can familiarize yourself with the project.

You're going to use:

- [Flask](http://flask.pocoo.org/docs/1.0/) for our web framework
- [Requests](http://docs.python-requests.org/en/master/) to grab data from [Tenor's GIF API](https://tenor.com/gifapi)

 Learn the basics of Flask and Requests. Both are easy to learn and these resources listed below are good resources and references for getting started: 
  * [Flask Megatutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) **Chaper 1-3 only**
  * [Routing with Flask](https://www.rithmschool.com/courses/flask-fundamentals/routing-with-flask)
  * [Requests Quickstart](http://docs.python-requests.org/en/master/user/quickstart/)

Before moving on, make sure to create a developer account and [request an API key](https://tenor.com/gifapi/documentation). 
   In `views.py` replace "Your API Key" with your actual API key in the code.
