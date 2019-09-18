# Git
Git has become a necessity in the open-source ecosystem.  Git is a distributed
version control system meaning that it helps software projects to remotely
collaborate on their project and track changes to their source code.  It is not
the only version control system in use but has become the defacto standard 
amongst open-source projects.  In order to prepare our students for 
participation in various group projects, we will introduce them to Git by 
covering some of the basic commands and uses.

## Setup
There are a number of ways that you could approach to using and teaching Git.  
I have found that most commonly, Git will be used to push to and pull from a 
remote repository; the most popular being www.github.com and www.gitlab.com.  
Both should allow you to setup free accounts and public repositories to aid in 
the teaching of the material.  It is by far the simplest method in my opinion 
and will get you up and running very quickly.

## For the Brave and Slightly Crazy
For my own edification, I decided to take a different approach and download the
Gitlab docker image and run that on my linux machine.  This however, could have
easily been done on a RaspberryPi as well.  The only criteria that I am aware
of is the server has to be Linux based, running docker, and can be reached
from other systems over the network.  Specifically, I suggest making sure ports
443, 80, and 22 are reacheable.

To launch the included (./docker-compose.yml)[./docker-compose.yml] file type: 
docker-compose up -d` from within the directory containing this file.

> **WARNING**: port 443, 80, and 22 may already be bound.

You'll need to shut down the conflicting services or launch on another machine.
While the ports on the docker image are configurable, to keep the git labs 
standardized, I decided to shut my own services down.  Specifically, I was 
already running openssh and therefore had to run `sudo sytemctl stop sshd`.

1. This will download the docker image and fire it up.  It may take some time
depending upon your download speeds.
1. You can run `docker ps` to validate that the image is running.
1. In the future, you can run `docker ps -a` find the gitlab instance, and run
   `docker start NAME` inserting the actual name of the container for *NAME*.
1. Add the following line to /etc/hosts: `127.0.0.1     gitlab.scoa.org`
1. Launch a web browser and browse to https://gitlab.scoa.org.
1. If this is your first time launching the docker image, it will prompt you
   to create a password for the *root* account.

### Create Users
1. Once logged in as *root*, click *Add people*.
1. I created student1, student2, etc...  You can then go in and edit those
   users to set their initial passwords.
1. Once those users log in, they will be prompted to change their passwords.

### Generate SSH Keys
Each user should generate ssh keys to add to their profiles using the included
guide: (ssh-GitLab.pdf)[./ssh-GitLab.pdf]
