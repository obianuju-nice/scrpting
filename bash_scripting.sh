
#!/bin/bash

#  file permissions execution of the entire script on the terminal
chmod 700 bash_scripting.sh

# comments in shell scripting 

# Environment VAriables
# Use Environment Variables to access system env variable
# Use uppercase letters for environment variable names to distinguish them from regular shell variables
#  PATH: A colon-separated list of directories where the shell looks for executable files.
#  HOME: The home directory of the current user.
#  USER: The name of the current user.
#  SHELL: The path to the current user's shell.
#  PWD: The current working directory.

# Set a new environment variable
export TRAINNG="Welcome to Shell Scripting with Nickos Training!"

# Accessing built-in environment variables
echo "User: $USER"
echo "Home Directory: $HOME"
echo "Current Shell: $SHELL"

# Accessing the custom environment variable
echo $MY_VAR
echo "My home or user directory is: $HOME"
 
# Exporting Variables: To make a variable available to child processes, use the export command.
export NAME="Mike"

# Use the printenv or env command to list all environment variables
# printenv

# Data types 

# 1. variables ( local  and global variables) Shell scripting primarily supports the following data types:
Strings: A sequence of characters. ex: "My name is Nice"  
Integers: Whole numbers. ex: age=20
Arrays: A collection of values indexed by numbers.

# name="Nice"
numbers=100
NAME="obianuju"
ORIGIN="nigerian"
location="london"

echo "my name is $NAME and my origin is $ORIGIN while my location is $location"

# Control Structures:( conditional statements using if else then fi )


if [[ $name==Nice ]]; then

  echo "The name exists"

elif [[ $name=obianuju ]]; then

    echo "No such name"

else 

   echo "Look for the name elsewhere"

fi 


# for loop  

# for i in {1..5}; do

#     echo $i

# done


# Read /capturing input from the  user and outputting data on the console 

# 3. Functions: this is a set of methods that passes args and return some output

# functions and returning values from functions

Hello_Learners() {

    learners='Hope you are doing great'

    echo "$learners"

}
return_function=$(Hello_Learners)

#  Passing arguments to functions a

# 4. Standad Input/Output 



# using stdin. stdout, stderr



# Redirection using > , >>, < , 2>, 



# 4. Error Handling



# Exit Status: Understanding $? and exit codes.



#  Using set -e and set -u: 



# 5. Arrayys
# Method 1: Declare and assign values
modules=(Docker Kubernetes aws Terraform Prometheus)
echo ${modules[0]}    # or echo "${Modules[0]}" 
echo ${modules[1]}
echo ${modules[2]}
echo ${modules[3]}
# echo ${modules[4]}

# Method 2: Declare an empty array and add elements/values
modules=()
modules[0]=Docker
modules[1]=Kubernetes 
modules[2]=terraform

# the for loop continues until it reads all the values from the MODULES
for courses in "$($MODULES)"; do
  echo The courses inside the modules are:  $(courses)
done

# 6. Scheduling Jobs (Scheduling jobs allows tasks to run automatically at specific times or intervals without manual intervention)

# use crontab -e to edit cron file and set up scheduled tasks.

#  Using at: Scheduling one-time jobs.

# 0 10 * * 1 /home/nice/NICKOS_DEVOPS/scrpting/bash_scripting.sh