# API_Imogi
=============

Common code for the Relational Databases and Full Stack Fundamentals courses

# Setting Up
Follow the instructions on installing Git, VirtualBox and Vagrant on your respective system.Some helpful links are listed below
* [Virtual Box](https://www.virtualbox.org/wiki/Linux_Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)

From the terminal run the following commands 
- Download the file using ```git clone http://github.com/<username>/fullstack-nanodegree-vm fullstack```
- This will give you a directory named ```fullstack``` that is a clone of your remote ```fullstack-nanodegree-vm``` repository.
- Then ```cd fullstack``` to enter into the directory just created
- Then run ```vangrant up```

Once it is up and running, type ```vagrant ssh```. This will log your terminal into the virtual machine, and you'll get a Linux
shell prompt. When you want to log out, type ```exit``` at the shell prompt. To turn the virtual machine off (without deleting
anything), type ```vagrant halt.``` If you do this, you'll need to run ```vagrant up``` again before you can log into it.

## Running the App
Navigate to the ```fullstack``` directory on your system and issue the following command
- Type ```python project.py``` and follow the instruction that is displayed on the command shell
- Type ```ctlr + c ``` to end the session
