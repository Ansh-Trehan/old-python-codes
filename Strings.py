def find(str,ch):
    index=0
    while(index < len(str)):
        if str[index]==ch:
            return index
        index+=1
    return -1

str1=input("Enter the string")
cha=input("Enter the character to be searched")
a=find(str1,cha)+1
print(a)
