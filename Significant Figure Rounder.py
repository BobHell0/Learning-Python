# Goal: Significant Figure-er

num = input("Input a number: ")

# Smart-Ass Removal
num_nodp = num.replace(".","")

while int(num.replace(".", "")) == 0:
    num = input("Please enter a non-zero number: ") 

if "." in num:
    num_1 = num.replace(".", "")

    while num_1.isdigit() == False or num.count(".") > 1:
        num = input("Please input a number:")
        num_1 = num.replace(".", "")

else:
    while num.isdigit() == False:
       num = input("Please input a number:") 
    while num[0] == "0":
        num = num[1:len(num)]

s_f = input("How many significant figures? ")

while s_f.isdigit() == False or s_f == "0":
    s_f = input("Don't be a donkey: ")

s_f = int(s_f)

# More s.f. than Digits 
if len(num) < s_f:
    if "." in num:
        num = num + s_f * "0"
    else:
        num = num + "." + s_f * "0"
        num_2 = num.replace(".", "")

# Integer Rounding
if not("." in num):
    if len(num) == s_f:
        print(num)
    else:
        num_front = num[0:s_f]
        num_back = num[s_f:len(num)]

        if int(num[s_f]) >= 5:
            num_front = int(num_front) + 1
    
        else:
            pass
    
        num_end = len(num_back)*"0"

        rounded = str(num_front) + num_end
        print(rounded)

# Decimal Rounding
else: 
    dp_pos = num.find(".") 

    # Check: is first s.f. before or after d.p.?
    zeropointcheck =  num[0:dp_pos]
    if "1" in zeropointcheck or "2" in zeropointcheck or "3" in zeropointcheck or "4" in zeropointcheck or "5" in zeropointcheck or "6" in zeropointcheck or "7" in zeropointcheck or "8" in zeropointcheck or "9" in zeropointcheck:
        
        if "." in num[0:s_f]:
            if len(num) - 1 < s_f:
                num = num + s_f*"0"
            elif len(num) - 1 == s_f:
                print(num)

            else:
                num_list = [num, num.replace(".",""), num.replace(".","")[0:s_f], num.replace(".","")[0:s_f + 1]]
                num_x = num.replace(".","")[0:s_f + 1]

                if int(num_x[-1]) >= 5:
                    num_sf = str(int(num.replace(".","")[0:s_f]) + 1)
                    
                    num_sf = num_sf + (len(num) - 1 - s_f) * "x"
                    
                    if len(num_sf.replace("x", "")) > s_f:
                        dp_pos += 1

                    num = num_sf[0:dp_pos] + "." + num_sf[dp_pos : len(num_sf)]
                    
                    num = num.replace("x","")
                    print(num)
                
                else: 
                    print(num[0:s_f+1])   

        else:
            num_front = num[0:s_f] 
            if int(num_1[s_f]) >= 5:
                num_front = int(num_front) + 1           
            else:
                pass
            
            num_back = num[s_f:dp_pos]
            num_end = len(num_back)*"0"
        
            print(str(num_front) + num_end)

    else: # 0.somethingsomething
        num_dp = num[dp_pos+1:len(num)]

        if len(num_dp) <= s_f:
            num_dp = num_dp + s_f * "0"

        for c in range(len(num_dp)): #finding where the first non-zero decimal place is
            if num_dp[c] == "0":
                pass
            else:
                first_nonzero = c
                break

        num_front = num_dp[first_nonzero:first_nonzero + s_f]

        if int(num_dp[first_nonzero + s_f]) >= 5:
            num_front = int(num_front) + 1
        else:
            pass
        
        print("0." + first_nonzero * "0" + str(num_front))
