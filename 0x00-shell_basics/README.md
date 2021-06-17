What I learned from this project

At the end of this project you are expected to be able to explain to anyone, without the help of Google:

General

-What does RTFM mean?
 READTHEFORKINGMANUAL.
-What is a Shebang
 A character sequence at the beginning of a script, also known as hashbang or pound-bang. Lots of the files in this dir is #!/bin/bash and that 
 instructs the machine to run bin/bash before the rest.

What is the Shell

-What is the shell
 The Shell delivers keyboard inputs to the OS to perform. They were the precursors to GUIs and bash is one of the most popular.
-What is the difference between a terminal and a shell
 Shell processes commands and returns output. Terminals run shell programs.
-What is the shell prompt
 It is where the user types commands. The shell prompt is also known as the command line. On Vim it is when you type colon (:).
-How to use the history (the basics)
 Up arrow. Greatest shortcut for bash.

Navigation

-What do the commands or built-ins cd, pwd, ls do
 cd is change directory, follow it with the directory name. pwd is print your current working directory. ls is list current directory. 
 Yes, these sentences bothered me cause I wanted to capitalize the first letter but you can't type Cd or Pwd.
-How to navigate the filesystem
 cd, ls, cd, ls... throw in 'ls -a' to see hidden files.
-What are the . and .. directories
 is current and .. is parent directory.
-What is the working directory, how to print it and how to change it
 The working directory is the current folder you are in. pwd is to change and refer above how to navigate or change it.
-What is the root directory
 The root is the highest or top directory in the hiearchy, it contains all other files.
-What is the home directory, and how to go there
 Say this in E.T.'s voice, "cd go home." The home dir is the login directory, or the repo of the user's personal files. 
 It is usually the first one you are inside once logging into the system.
-What is the difference between the root directory and the home directory of the user root
 The home directory is in the root. The root is king of all. Root is topmost level, referred by '/.' while home is the user and has folders like 
 Documents or Music or Pictures and is referred to by '~'.
-What are the characteristics of hidden files and how to list them
 They begin with a '.' usually and they are listed with the -a flag.
-What does the command cd - do
 cd - brings your back to the previous directory

Looking Around

-What do the commands ls, less, file do
 ls lists the files and dir in the current working dir. less views the file instead of opening them. file shows the type of data contained in a computer file.
-How do you use options and arguments with commands
 You would use the option indicator '-' and that would allow the use of flags. Arguments, or parameters, are the targeted file names or dir or 
 other stuff you are trying to manipulate. Extra C facts (argc contains the number of arguments passed from the command line and argv 
 contains the pointer to strings containing the names of these arguments).
-Understand the ls long format and how to display it
 la -l. The long format shows the file permissions, owner, group, size in bytes, modification time, and file name.

A Guided Tour
 
-What does the ln command do
 It creates a hard link to an existing file. If it has the flag -s then it is a symbolic link. This allows multiple filenames to be
-What do you find in the most common/important directories
 Answer in this link. We got all the good stuff in this link, scroll down to important directories. Theres boot which helps boot the process and kernel, 
 bin with its binary stuff, tmp, usr, and tons of other important ones
-What is a symbolic link
 Also known as soft link or symlink. This is a term for any file that contains a reference to another file or dir in the form of an absolute or relative path. 
 Basically it makes text string that is connected to a target and it is like a pointer. Symbolic links can point to non-existant files.
-What is a hard link
 Hard links cannot point to nothing. They must always refer to an existing file. Hard links .
-What is the difference between a hard link and a symbolic link
 Hard is hard. Really connected. If the original goes so does the hard link. For symbollic, there can be an orphaned or dangling link. 
 Symbolic links can exist on their own and arn't completely dependent on the target file for existing

Manipulating Files

-What do the commands cp, mv, rm, mkdir do
 cp copies. mv moves or renames. rm removes files or directories. mkdir makes directories.
-What are wildcards and how do they work
 The asterisk, or star, or multiply sign, is a wild card. Anything can be put in. It can be everything or anythinng. It can be super specific if you 
 follow proper syntax or regex stuff.
-How to use wildcards
 Star card is most common. It cna be anything, even zero chars. the question mark wild card means that can be any one single character. So c?
 t can be cat or cot or cut. Square brackets wild cards are any of the caracters inside the bracket. So common uses are vowels [aeiou]. 
 Hyphens inside mean include inbetween like a-g means a through g. [a-dog] would mean to look for anything that stats with a through d or 
 begins with o or g.[0-9][0-9][0-9] looks for all 3 digit numbers.

Working with Commands

-What do type, which, help, man commands do
 type displays information about command type. which shows full path of commands. help shows a ton of different commands. Typing in help onto the 
 command line is self-ex planatory. man shows manuals. type man and it will prompt which page number.
-What are the different kinds of commands
 Type "type type" or "type alias" to see different types. Some might be a shell builtin, others are locaed in important directories.
-What is an alias
 A command that enables a replacement of a word by another string. Common for abbreviating a system command.
-When do you use the command help instead of man
 help is a bash command. It uses internal bash structures to store and retrieve info about bash commands. man is a macro that uses troff (geoff). 
 The output of processing a file is sent to a pager by the an by default. info is a text-only viewer for archives in the output format of Texinfo

Reading Man Pages

-How to read a man page
 NAME is the name of the command or function, followed by a short description. SYNOPSIS is a formal description of how to run it and what command line 
 options it accepts. Usually a list of arguments and which header file contains the definition
-What are man page sections
 The numbers correspond to what section of the manual that the page is from. 1 is user commands, 8 is sysadmin, etc.
-What are the section numbers for User commands, System calls and Library functions
 1 is user commands, 2 is system calls, 3 is C library, 4 is devices and special files, 5 is file formats and conventions, 6 is Games et. al., 7 is 
 miscellanea, 8 is system administration tools and daemons. Additional sections exist.

Keyboard Shortcuts for Bash

-Common shortcuts for Bash
 Ctrl+c to kill current process via SIGINT request. Ctrl+s stops screen output but wil still run process. Ctrl+l clears screen. Ctrl+a is beginning of 
 line, ctrl+e is end of line. Alt+b is go back a word, alt+f go forward one word. Alt+d deletes all chars after cursor on current line. Ctrl+_ is undo. 
 Ctrl+y is paste/yank and ctrl+w cuts word before cursor, ctrl+u cuts part of line before cursor, ctrl+k cuts part of line after cursor.

LTS

-What does LTS mean?
 Long Term Support. It is the mindset that LTS is enterprise focused, compatible with new hardware, and tested more.

Each scripts and their output

-Script 0 - Write a script that prints the absolute path name of the current working directory.
-Script 1 - Display the contents list of your current directory.
-Script 2 - Write a script that changes the working directory to the user’s home directory.
-Script 3 - Display current directory contents in a long format.
-Script 4 - Display current directory contents, including hidden files (starting with .). Use the long format.
-Script 5 - Display current directory contents. Long format, with user and group IDs displayed numerically, And hidden files (starting with .).
-Script 6 - Create a script that creates a directory named holberton in the /tmp/ directory.
-Script 7 - Move the file betty from /tmp/ to /tmp/holberton.
-Script 8 - Delete the file betty.
-Script 9 - Delete the directory holberton that is in the /tmp directory.
-Script 10 - Write a script that changes the working directory to the previous one.
-Script 11 - Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the
 parent of the working directory and the /boot directory (in this order), in long format.
-Script 12 - Write a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.
-Script 13 - Create a symbolic link to /bin/ls, named _ls_. The symbolic link should be created in the current working directory.
-Script 14 - Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory. You can consider that all HTML files have the extension .html.
-Script 15 - Create a script that moves all files beginning with an uppercase letter to the directory /tmp/u. You can assume that the directory /tmp/u will exist when we will run your script.
-Script 16 - Create a script that deletes all files in the current working directory that end with the character ~.
-Script 17 - Create a script that creates the directories welcome/, welcome/to/ and welcome/to/holberton in the current directory. You are only allowed to use two spaces in your script, not more.
-Script 18 - Write a command that lists all the files and directories of the current directory, separated by commas (,). Directory names 
 should end with a slash (/). Files and directories starting with a dot (.) should be listed. The listing should be alpha ordered, except for the 
 directories . and .. which should be listed at the very beginning. Only digits and letters are used to sort; Digits should come first. You can 
 assume that all the files we will test with will have at least one letter or one digit. The listing should end with a new line.
-Script holberton - Create a magic file holberton.mgc that can be used with the command file to detect Holberton data files. Holberton data files always 
 contain the string HOLBERTON at offset 0.

Limitations of these projects:

-Allowed editors: vi, vim, emacs
-All your scripts will be tested on Ubuntu 20.04 LTS
-All your scripts should be exactly two lines long ($ wc -l file should print 2)
-All your files should end with a new line (why?)
-The first line of all your files should be exactly #!/bin/bash
-A README.md file at the root of the alx-system_engineering-devops repo, containing a description of the repository
-A README.md file, at the root of the folder of this project, describing what each script is doing
-You are not allowed to use backticks, &&, || or ;
-All your scripts must be executable. To make your file executable, use the chmod command: chmod u+x file. Later, we’ll learn more about how to utilize this command.
