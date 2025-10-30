def hypotenuse(x,y):
  hyp = x**2 + y**2
  return hyp**0.5
x = float(input("Enter the length of the adjacent side:"))
y = float(input("Enter the length of the opposite side:"))
h = round(hypotenuse(x,y),2)
print("The length of the hypotenuse is ",h) 
