#it is a bubble Sort

#This is the string that we will to sort
String = [8,5,6,3,9,2,5,9,4,1,3,2,33,55,2,100,3,4,98]
print(String)
flag=True #inizialace flag with value true
count=0;
i=0;
while flag==True: #While that someone exchanges exist
    flag=False #inizialace in false to validate if in the next round exist a exchange
    i=0
    #
    for i in range(len(String)):
        if i != len(String)-1:
            if(String[i]>String[i+1]):
                aux=String[i]
                aux2=String[i+1]
                #exchanges the position i with the value of the position i+1
                String[i]=aux2
                #exchanges the position i+1 with the value of the position i
                String[i+1]=aux
                #increase the value of count to see how many exchanges were made
                flag=True#has a exchange


print(String)#The string now ordered
