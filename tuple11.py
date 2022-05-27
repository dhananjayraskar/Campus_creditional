#Tuple = store multiple data items in a single variable
#ordered, unchangable, allows duplications, indexed

Cities =tuple(("Mumbai","Chennai","Delhi",50, 50.56, True, False))
print(Cities)
# print(type(Cities))

# "Mumbai" , "Chennai" , "Delhi", 50, 50.56, True, False
# 0            1           2       3   4      5      6
# -7            -6         -5      -4   -3    -2     -1

print(Cities[4])
print(Cities[-5])

