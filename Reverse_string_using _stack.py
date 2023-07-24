# Create empty stack
stack = [] 
string = input("Enter a string: ")  #user string apse
for char in string:    #ahiya apde darek char ne stack ma push karisu
  stack.append(char)  
reversed_string = ""  #ani andar apde rev string add karisu
while stack:
  reversed_string += stack.pop() #stack mathi nikdine ne a join thai jase reverse string ne
   
