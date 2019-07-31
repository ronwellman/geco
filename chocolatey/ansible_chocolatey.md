# Ansible and Chocolatey
Ansible is an automation framework to configure and maintain state on remote 
machines.  Chocolatey acts as a software repository for the Windows operating
system.  By pairing them up together, you can remotely install software and
ensure machine state is maintained.

The following steps assume a Linux computer running Ansible, Windows 10 machines running Powershell 5 or later, network connectivity between the machines, and an Internet connection.

Steps 1-7 below only need to be completed during initial setup assuming IP addresses within the hosts file remain accurate.  From then on, new playbooks can be added for additional settings and software installs.

### WinRm.ps1
1. Copy the WinRm.ps1 to each Windows machine making a
   not of where it is saved.  This script will be used to:
    * setup *WinRM* on the system
    * generate self-signed certificates
    * enable CredSSD

1. Execute WinRM.ps1
    * Hit the Windows key and type *cmd*
    * You may have to click on the *Apps* tab
    * Right click the Command Prompt and select *Run as administrator*
    * `powershell.exe -ExecutionPolicy ByPass -File WinRm.ps1 -EnableCredSSP -DisableBasicAuth -SkipNetworkProfileCheck`

1. Check the Listener
    * To validate the two listeners are up:
    * `winrm enumerate winrm/config/Listener`

1. IP Address
    * Record the system's IP address by running *ipconfig*

### Ansible Configuration
1. Ansible Machine (Linux)
    * Install requisite packages
        * `sudo apt install ansible python-pip`
        * `pip install pywinrm[credssp]`

1. Ansible Hosts
    * Edit the included *hosts.yml* file
        * Add the IP addresses of the Windows computers
        * Add the Username and Password of the Windows computers
    * Encrypt the *hosts.yml* file
        * `ansible-vault encrypt hosts.yml`
        * enter a password when prompted
    * To edit the encrypted hosts file in the future
        * `ansible-vault edit hosts.yml`

1. Verify Connectivity
    * `ansible win --ask-vault-pass -i hosts.yml -m win_ping`
    * enter the password when prompted
    * You should get back a SUCCESS message

### Ansible Playbook
1. Run a Playbook
    * `ansible-playbook --ask-vault-pass -i hosts.yml playbook.yml`
    * This will install Chocolatey and any programs specified in the playbook
    * Most programs will show up in the start menu.  For those that don't, they are often located in *C:\ProgramData\chocolatey*
    * If run again, Ansible can tell that Chocolatey as well as all the programs specified are already installed
