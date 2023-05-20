para =[]
print("Enter the sentense or para : ")
while True:
    line=input()
    if line :
        para.append(line)
    else :
        break
output='\n'.join(para)
print(output)



# string mainpulation

char="sample"

print(char) # to print all the letters

print(char[0:3]) #to print from to from only 

n=len(char)-1
print(char[:n]) #to remove the last charcater 

print(char[1:]) #to remove the first charcater 

print(char[::-1]) # to reverse the string 