#The exercise consist in draw a square with a variable n that represent the
#number of asterisks that form the square*/


#the first is ask the value of n
n=int(input());
#draw the horizontal line above
for i in range(n):
    print '* ',

print(" ")
#draw the right and left vertical lines
j=1
while j <= n-2:
    for k in range(n):
        #This condition is for the left line
        if k == 0:
            print '* ',
        #This condition is for the right line
        elif k == n-1:
            print'* ',
        #This condition is for the empty places
        else:
            print'  ',
    print("")
    j+=1

i=0
#draw the horizontal line below
for i in range(n):
    print '* ',
