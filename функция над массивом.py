def modify_list(lst):
    i = 0
    le = len(lst)
    while i<le:
        if(lst[i]%2!=0):
            del lst[i]
            le -=1
        else:
            lst[i]=int(lst[i]//2)
            i +=1
        
            
lst = [-1,-1]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
