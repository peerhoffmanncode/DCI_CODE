### Algo - LOOP in two versions 

sum = 0                                 # set var to 0
count = 0                               # set var to 0

max_rounds = int(input("enter value of rounds : "))                         # let the user decide how many loops will be done

for count in range(1, max_rounds + 1):                                      # start of FOR LOOP
    user_input = int(input("Enter a number : "))                            # let the user input a value
    sum = sum + user_input                                                  # sum up the value with teh var sum
    print("current value: " + str(sum) + " current round " + str(count))    # print out the current state for every loop !

### LOOP END
print("final state: " + str(sum) + " this is my result" )       # print out the final sum once !





# RESET ALL VARIABLES !

sum = 0                                 # set var to 0
count = 0                               # set var to 0

max_rounds = int(input("enter value of rounds : "))                         # let the user decide how many loops will be done
 
while (count < int(max_rounds)):                                            # start of WHILE LOOP
    user_input = int(input("Enter a number : "))                            # let the user input a value
    sum = sum + user_input                                                  # sum up the value with teh var sum
    count = count + 1
    print("current value: " + str(sum) + " current round " + str(count))    # print out the current state for every loop !
    
    
### LOOP END
print("final state: " + str(sum) + " this is my result" )       # print out the final sum once !