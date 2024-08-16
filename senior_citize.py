data = ["7868190130M7522", "983498123F4522"]
c=0
for i in data:   #this will run through the data list
    age_Str=int(i[-4:-2])   #we are converting the list into string

    if age_Str > 60:
        c+=1

print(c)    #return counter
