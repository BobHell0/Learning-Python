#Project: Manual Number Rounder:

num = input("Input a decimal number: ")
if num.count(".") == 1:
    num_1 = num.replace(".","")

    if num_1.isdigit() == True:
        p = num.find(".")
        len = len(num)
        num_dp = num[p+1:len]
 
        num_wn = num[0:p]

        i_s = num_dp[0]
        i_i = int(i_s)

        if i_i >= 5:    #Round up
            print(int(num_wn) + 1)
        else:           #Round down
            print(int(num_wn))
    else:
        print("Input a decimal number")

else:
    print("Input a decimal number")