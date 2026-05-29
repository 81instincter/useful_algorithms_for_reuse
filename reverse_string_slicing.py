expr = "45+34*94/34"

i = len(expr) - 1

# Move backwards while characters are digits or decimal points
while i >= 0 and (expr[i].isnumeric() or expr[i] == '.'): # If expr[i] is a non-numeric character that is not a decimal, split the string 
    i -= 1

# Keep everything up to and including the operator
expr = expr[:i+1]

print(expr)