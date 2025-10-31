def hypotenuse(x,y):
  hyp = x**2 + y**2
  return hyp**0.5
x = float(input("Enter the length of the adjacent side:"))
y = float(input("Enter the length of the opposite side:"))
h = round(hypotenuse(x,y),2)
print("The length of the hypotenuse is ",h) 

#pythagoras in 3d
def length(x,y,z=0):
    """Return the length of the line segment between points (0, 0, 0) to (x, y, z).
    If no z-axis parameter is specified, then data is assumed to exist in
    a two-dimensional plane."""
    sq = x**2 + y**2 + z**2
    return sq**0.5
x = float(input("Enter value of x: "))
y = float(input("Enter value of y: "))
z = float(input("Enter value of z: "))
line_segment = round(length(x,y,z),2)
print("the length of the line segment between the origin and", (x,y,z), "is", line_segment)
