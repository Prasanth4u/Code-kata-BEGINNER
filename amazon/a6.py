"""
You are given a number with duplicate digits your task is to remove the immediate duplicate digits and print the result

Input Description:
You are given a long string of digits

Output Description:
Print the desired result print -1 if result length is 0

Sample Input :
1331
Sample Output :
11
"""

#program
def removeRecur(n):
     
    # Store first digits as previous digit
    prev_digit = n % 10
 
    # Initialize power
    pow = 10
    res = prev_digit
    
    # Iterate through all digits of n, note
    # that the digits are processed from
    # least significant digit to most
    # significant digit.
    while (n):
         
        # Store current digit
        curr_digit = n % 10
 
        if (curr_digit != prev_digit):
             
            # Add the current digit to the
            # beginning of result
            res += curr_digit * pow
 
            # Update previous result and power
            prev_digit = curr_digit
            pow *= 10
 
        # Remove last digit from n
        n = int(n / 10)
     
    return res

# Driver Code
if __name__ == '__main__':
    n = 32122
    print(removeRecur(n))



