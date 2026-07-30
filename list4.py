numbers=[1,2,3,4,5,6,5,2]
new_list=[]
for i in  numbers:
    if i not in new_list:
        new_list.append(i)
        print(new_list)