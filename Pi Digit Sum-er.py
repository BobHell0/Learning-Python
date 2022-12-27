
#Pi Digit Sum-er [First 101 digits]
    #I'm taking 3 to be the first digit of pi if ur mad lol
pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

num_digits = int(input("How many digits of pi should I add? "))

while num_digits > 101 or num_digits <= 0:
    num_digits = int(input("Enter a number greater than 0 and less than or equal to 101: "))

sum = 0

pi_e = pi.replace(".","")
pi_e = pi_e[:num_digits]


for i in pi_e:
    sum += int(i)

print("Sum is " + str(sum))

