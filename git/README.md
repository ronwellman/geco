# Git
Git has become a necessity in the open-source ecosystem.  Git is a distributed
version control system meaning that it helps software projects to remotely
collaborate on their project and track changes to their source code.  It is not
the only version control system in use but has become the defacto standard 
amongst open-source projects.  In order to prepare our students for 
participation in various group projects, we will introduce them to Git by 
covering some of the basic commands and uses.

## Setup
There are a number of ways that you could approach using and teaching Git.  
I have found that most commonly, Git will be used to push to and pull from a 
remote repository; the most popular being (https://www.github.com)[https://www.github.com] 
and (https://www.gitlab.com)[https://www.gitlab.com].  Both should allow you to 
setup free accounts and public repositories to aid in the teaching of the 
material.  It is by far the simplest method in my opinion and will get you up 
and running very quickly. It does however, require different email accounts for
each student

## For the Brave and Slightly Crazy
For my own edification, I decided to take a different approach and download the
Gitlab docker image and run that on my Linux machine.  This however, could have
easily been done on a RaspberryPi as well.  The only criteria that I am aware
of is the server has to be Linux based, running docker, and can be reached
from other systems over the network.  Specifically, I suggest making sure ports
443, 80, and 22 are reacheable.

To launch the included (./docker-compose.yml)[./docker-compose.yml] file type: 
`docker-compose up -d` from within the directory containing this file.

> **WARNING**: port 443, 80, and 22 may already be bound.

You'll need to shut down the conflicting services or launch on another machine.
While the ports on the docker image are configurable, to keep the git labs 
standardized, I decided to shut my own services down.  Specifically, I was 
already running OpenSSH and therefore had to run `sudo sytemctl stop sshd`.

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

`ssh-keygen -o -b 4096 -C student1@scoa.org`

#### Windows 10
Windows 10 now comes pre-installed with OpenSSH which you'll need to generate
ssh keys.  However, it does not come with Git.  You can open a browser and
navigate to (https://git-scm.com/downloads)[https://git-scm.com/downloads] to
download Git and install it. I recommend accepting all of the defaults during
installation.

This will attempt to store keys at c:\Users\USERNAME/.ssh/id_rsa which does not
exists.  I suggest you create a '.ssh' folder and point to it when generating
the keys.  From the command line you can run `type id_rsa.pub` and copy out the
value.  You'll need this when setting up the

#### Linux
It is very rare to not have OpenSSH and Git already installed on a modern Linux
distro.  If for some reason it is not, it's probably a `yum install`, `dnf
install`, or `apt install` away.

### Generate Gitconfig
The gitconfig file tells git various settings to use.  The below settings 

```
git config --global user.name "Student1"
git config --global user.email "student1@scoa.org"
```

Additionally, I also prefer setting no fast forward.  When you *MERGE* back
into master, depending upon how git is configured, it will typically condense
log history.  In order to preserve this, I put the following in my gitconfig:

```
git config --global merge.ff=false
```
