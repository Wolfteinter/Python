#it is a bubble Sort

#This is the string that we will to sort
String = [8,5,6,3,9,2,5,9,4,1,3,2,33,55,2,100,3,4,98]
print(String)
flag=False #inizialace flag with value true
count=0;
i=0;
while flag!=True: #While that someone exchanges exist
    count=0#inizialace count in 0  to validate a new roand
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
                count+=1;
    #if count is equals to 0 is because there were no exchanges
    if(count==0):
        #THis is the condition to stop to do exchanges
        flag=True
    else:
        flag=False

print(String)#The string now ordered
