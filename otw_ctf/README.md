# OTW_CTF
In this lab, we will introduce the club to Capture The Flag (CTF) exercises via [Over the Wire](http://overthewire.org/).  Using the first couple levels of the Bandit wargame, we'll challenge and demonstrate ways to reveal the flag (the next level's password) in order to expose the club to additional Linux commands and hopefully spark some interest in future activities of this type.  Although only the first 10 or so levels will be covered in this lab, students are encouraged to continue pressing on.

## Rules of the Road
1. Students can use any resource at hand to attain the password short of merely finding passwords posted to the Internet.
2. Demonstrate bringing up man pages and searching within them.  The *ssh* command would be an excelant starting point to show them how to find out how to specify the port number.
3. Students should be given 5 - 10 minutes to attempt to solve a level before a mentor demonstrates the answer.  It is assumed that most of the students will not be able to get every answer.  This is to be expected.
4. Students are not required to wait on the mentor before proceding to the next level.  However, questions about future levels will be trumped by questions from other students about the current level.
5. Impress on the students that there may be multiple ways of getting to the flag and that's perfectly fine.  If a student wants to talk about their particular solution, ask for a demonstration.

## Setup
The only two requirements are the following:
1. A computer with an internet connection.
2. The ability to establish an SSH connection.
3. A web browser to find out the task to complete at each level. [Bandit0](http://overthewire.org/wargames/bandit/bandit0.html)

### Windows
For computers running the Windows operating system, it is suggested that students download and install [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).

### Linux and Mac
Both of these operating systems have SSH clients built into them.  Ensure students know how to access the terminal and demonstrate specifying the username and port number of an SSH connection.  For example, to connect to the Over the Wire server via SSH over port 2220 for level 0 (bandit0):

```bash
ssh -p 2220 bandit0@bandit.labs.overthewire.org
``` 

## Level 0

#### UN
bandit0

#### PW
bandit0

#### Procedure

```bash
ls
cat readme
``` 

## Level 1

#### UN
bandit1

#### PW
boJ9jbbUNNfktd78OOpsqOltutMc3MY1

#### Procecure

```bash
ls
cat ./-
```

## Level 2

#### UN
bandit2

#### PW
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

#### Procedure

```bash
ls
cat 'spaces in this filename'
```

## Level 3

#### UN
bandit3

#### PW
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

#### Procedure

```bash
ls
cd inhere
ls -la
cat .hidden
```

## Level 4

#### UN
bandit4

#### PW
pIwrPrtPN36QITSp3EQaw936yaFoFgAB

#### Procedure

```bash
ls
cd inhere
```

You could run *file* against each file one by one.

```bash
file ./-file00
file ./-file01
...
file ./-file07
```

Alternatively you could loop through them all with a script.

```bash
for f in `ls`; do
file ./$f;
done
```

All of this will reveal file07 as the ascii file.

```bash
cat ./-file07
```

## Level 5

#### UN
bandit5

#### PW
koReBOKuIDDepwhWk7jZC0RTdopnAYKh

#### Procedure

```bash
ls
cd inhere
ls
```

Students are presented with a number of folder containing a number of different files. Checking for a specific file of a specific length works best with the find command.

```bash
find ./ -size 1033c
```

This reveals ./maybehere07/.file2 as the only file of that length.

```bash
ls -l ./maybehere07/.file2
```

Shows that it meets all the criteria.

```bash
cat ./maybehere07/.file2
```

## Level 6

#### UN
bandit6

#### PW
DXjZPULLxYr17uwoI01bNLQbtFemEgo7

#### Procedure

```bash
find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
```

## Level 7

#### UN
bandit7

#### PW
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

#### Procedure

```bash
cat data.txt | grep millionth
```

## Level 8

#### UN
bandit8

#### PW
cvX2JJa4CFALtqS87jk27qwqGhBM9plV

#### Procedure

```bash
sort data.txt | uniq -u
```

## level 9

#### UN
bandit9

#### PW
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

#### Procedure

```bash
strings data.txt | grep ==
```

## Level 10

#### UN
bandit10

#### PW
truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

#### Procedure

```bash
cat data.txt | base64 -d
```

## Level 11

#### UN
bandit11

#### PW
IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

#### Procedure

Option 1 - Python

```bash
cat data.txt
python3
```

Copy the contents of data.txt from above into a variable called message.

```python3
message = 'Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh'
message.encode('rot-13')
```

Option 2 - tr.

```bash
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

## Level 12

#### UN
bandit12

#### PW
5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

#### Procedure

Create a temporary directory.

```bash
mktemp
```

Move into the new directory and copy the data file.

```bash
cd /tmp/tmp.THENEWDIRECTORY
cp ~/data.txt ./
```

Test the file type:

```bash
file data.txt
```
The file is initially a hexdump of the original file.  To reverse it:

```bash
xxd -r data.txt data
```

Test the file type:

```bash
file data
```

If it's a tar archive:

```bash
mv data data.tar
tar -xf data.tar
```

If it's a gzip archive:

```bash
mv data data.gz
gunzip data.gz
```

If its's a bzip2 archive:

```bash
mv data data.bz2
bzip2 -d data.bz2
```

Continue checking the type, renaming, and decompressing.  You will go through a number of interations.  Eventually, you will be left with an ascii file.

```bash
cat data.txt
```

## Level 13

#### UN
bandit13

#### PW
8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

#### Procedures
This following procedures require you to copy an ssh key to your local machine and use that to access bandit14.  There will be different procedures for Windows and Mac/Linux/UNIX.

```bash
cat sshkey.private
```

Copy and paste the contents into a file called bandit14.key.

##### Windows
You'll need to use Putty Key Generator to load the key into a usable Putty form.  Documentation can be found [here](https://support.rackspace.com/how-to/log-into-a-linux-server-with-an-ssh-private-key-on-windows/).

##### Mac/Linux/UNIX
Update permissions to the file so that only the owner can access it.

```bash
chmod 0600 bandit14.key
```

Reference the new key when you ssh into the bandit server:

```bash
ssh -p 2220 -i bandit14.key bandit14@bandit.labs.overthewire.org
```

## Level 14

#### UN
bandit14

#### PW
*bandit14.key* (ssh key access)

Once logged in:

```bash
cat /etc/bandit_pass/bandit14
```

This reveals: 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

#### Procedure

```bash
echo "4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e" | nc localhost 30000
```

## Level 15

#### UN
bandit15

#### PW
BfMYroe26WYalil77FoDi9qh59eK5xNr
