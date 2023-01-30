#Write a program that finds the duplicate elements in an array.
arr=[1,2,3,4,5,1,2,7,8,8]
l=[]
for i in arr:
    if i not in l:
        l.append(i)
    else:
        print(i)
    
    

        

        
        
    
