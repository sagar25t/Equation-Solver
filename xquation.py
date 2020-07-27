print ("Enter the co-efficients of equations in following manner : \n co-efficient of x (a), co-efficient of y (b), co-efficient of z (c), constant term (d) where : ")
print ("ax + by + cz = d ")
print ("")

a1, b1, c1, d1 = map(int,input("Enter the co-efficients of equation-1 : ").split(" "))
a2, b2, c2, d2 = map(int,input("Enter the co-efficients of equation-2 : ").split(" "))
a3, b3, c3, d3 = map(int,input("Enter the co-efficients of equation-3 : ").split(" "))

Det = a1*(b2*c3 - b3*c2) - a2*(b1*c3 - b3*c1) + a3*(b1*c2 - b2*c1) 

M11 = b2*c3 - b3*c2
M12 = -(a2*c3 - a3*c2)
M13 = a2*b3 - a3*b2
M21 = -(b1*c3 - b3*c1)
M22 = a1*c3 - a3*c1
M23 = -(a1*b3 - a3*b1)
M31 = b1*c2 - b2*c1
M32 = -(a1*c2 - a2*c1)
M33 = a1*b2 - a2*b1

A = [[M11, M21, M31], [M12, M22, M23], [M13, M23, M33]]

B = [[d1], [d2], [d3]]

x = A[0][0]*B[0][0] + A[0][1]*B[1][0] + A[0][2]*B[2][0]
y = A[1][0]*B[0][0] + A[1][1]*B[1][0] + A[1][2]*B[2][0]
z = A[2][0]*B[0][0] + A[2][1]*B[1][0] + A[2][2]*B[2][0]

print(f"x = {x/Det}")
print(f"y = {y/Det}")
print(f"z = {z/Det}")