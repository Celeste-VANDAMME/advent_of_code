# MD5 hash encryption:
import hashlib

# Global variables:
global SECRET_CODE;         SECRET_CODE = "ckczppom"
global MAX_LOOP_ITERATION;  MAX_LOOP_ITERATION = 100000000000000

# Hash encryption bruteforce:
i = 0
valueFound = False
while i <= MAX_LOOP_ITERATION:

    loopCode_trial = SECRET_CODE + str(i)
    # Print the tried code:
    # print(loopCode_trial)
    
    md5_encryption = hashlib.md5( loopCode_trial.encode() )
    hexa_md5_value = md5_encryption.hexdigest()

    if hexa_md5_value[:6] == "000000":
        valueFound = True
        break
    
    # END OF THE LOOP:
    i += 1
    
if valueFound:
    print("A value for the MD5 hexa code has been found!")
    print("Lowest int. value: ", i)
    print("Total code: ", loopCode_trial)

else:
    print("No values were found in the loop.")
    print('Try to increase the "MAX_LOOP_ITERATION" value to increase your chance of finding the code.')
    
    