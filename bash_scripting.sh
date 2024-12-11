
#!//bin/ bash

#  file permissions execution of the entire script on the terminal

# chmod + x linux.script

# chmod + x linux.sh



# 1. variables and Data types

name="Nice"

NAME="obianuju"

ORIGIN="nigerian"

location="london"



echo "my name is $NAME and my origin is $ORIGIN while my location is $location"



# Using read to capture user input,





# Environment Variables to access system env variable



#  Variables scope:  local  and global variables



# 2. Control Structures:

# conditional statements using if else then fi

if [[ $name==Nice ]]; then

  echo "The name exists"

elif [[ $myname!=Nice ]]; then

    echo "No such name"

else 

   echo "Look for the name elsewhere"

fi 



# for loop  

for i in {1..5}; do

    echo $i

done



# while loop

while [ condition ]; do

    # commands

done



# 3. Functions: this is a set of methods that passes args and return some output

# functions 

Hello_Learners() {

    learners='Hope you are doing great'

    echo "$learners"

}

return_function=$(Hello_Learners)



# 4. Standad Input/Output 



# using stdin. stdout, stderr



# Redirection using > , >>, < , 2>, 



# 4. Error Handling



# Exit Status: Understanding $? and exit codes.



#  Using set -e and set -u: 



# Enabling strict mode for scripts.



# 5. Arrayys

modules=(Docker Kubernetes aws Terraform Prometheus)



echo &{modules[0]}

echo &{modules[1]}

echo &{modules[2]}

echo &{modules[3]}



#  OR USE BELOW ONE

echo "${Modules[0]}" 

echo "${Modules[@]}" 

echo "${!Modules[@]}"          # Keys of all modules, space-separated

# the for loop continues until it reads all the values from the MODULES



for courses in $MODULES

do

  echo “The courses inside the modules are: $courses”

done



# 6. Scheduling Jobs



# use crontab -e to edit cron file and set up scheduled tasks.

#  Using at: Scheduling one-time jobs.






