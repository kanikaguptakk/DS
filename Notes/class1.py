print("Hello World")
#Variable- It is like a container which can be used to store different types of values.
# Variable naming convection- 1. A variable name must start with a letter or the underscore character.
#2. A variable name cannot start with a number.
#3. A variable name can only contain alpha-numeric characters and underscore (A-z, 0-9, and _)
a=98
print(a)
print("a")
# Type of a variable 
type(a)
b=c=d=2
print(b)
e,f,g=4,3,4
print(e)
# Data Types- 
# 1. Text Type- str
# 2. Numeric Types- int, float, complex
# 3. Sequence Types- list, tuple, range
# 4. Mapping Type- dict
# 5. Set Types- set, frozenset
# 6. Boolean Type- bool
# 7. Binary types- bytes, bytearray, memoryview
# 8. None Type- Nonetype
x=5j
type(x)    #comlex data type
print(a+b)
f=a+b
print(f)
A,B,C,D,E=1,2,3,4,5
print(A+B-C/D*E)

p="Kanika"
q="Gupta"
print(p+" "+q)  
# List are used to store multiple iteams in a single variable. List iteams are ordered, 
# changeable and allowed to store duplicate values. List are denoted by [].
y=[1, "Grapes", 55, 5j, True, "Apple"]
print(y)
type(y)
print(len(y))
print(y[1:5])
print(y[-5:-2])
print(y[-2:-5])
y[1]="Human"
print(y)

#Functions- insert, append, remove, pop
#Insert function is used to add items on a specific index.
y.insert(2, "Bird")
print(y)
y.insert(5, 77j)
print(y)
#Append function add items at the end of the list.
y.append("Mumma")
print(y)
y.append(6j)
print(y)
y.append("Grapes")
print(y)
y.append("Grapes")
print(y)
y.remove("Grapes")
print(y)
#pop- we use index number, instead of the item name to remove
y.pop(10)
print(y)
print(y[1:5:1])
print(y)
#Tuples- Tuples are used to store multiples items in a single variable. Tuples are immutable(unchangeable).
# Tuples are denoted by (). They are ordered. It allows duplicate values. 
w=("Hen", 44, 5j, False, "Goat")
print(w)
type(w)
print(w[1])
print(w[1:5])

#Type Conversion
t=("tree", "wood", 55, 5j, True)
r=list(t)
r[1]="branch"
q=tuple(r)
print(q)
del q

# Set- Set is also used to store multiple iteams. 
# Set is immutable, unordered, and unindexed and it doesn't allow duplicate values. It is enclosed by {}. 
g={"fan", "light", "cooler", "light"}
type(g)
print(g)
print(len(g))

# To acces the items -
for x in g:
    print(x)
K={"girl", "boy", 44, 5j, True, "Men", "Women"}    
print("girl" in K)
print("man" in K)
T=("girl", "boy", 44, 5j, True, "Men", "Women")    
print("men" in T)
print("Men" in T)
# T.add("hen")
# print(T)  # Tuple is ordered same with List 
K.add("hen")
print(K)   # Set is unordered

# Update function-to merge 2 sets
G={"girl", "fan", 44, 5j, True, "Men", "Women"}
H={False, 44j}
G.update(H)
print(G)
# F=("girl", "fan", 44, 5j, True, "Men", "Women")
# E=(False, 44j)
# F.update(E)
# print(F)      No merging in tuple

D={"girl", "gen", 44, 5j, True, "Men", "Women"}
B=(33, False)
D.update(B)
print(D)
# B.update(D)
# print(B)   # no merging in tuple-only possible in set 
C={"bat", 33, True, 4j, "ball"}
S=("bat", False)
C.update(S)
print(C)    # the item is not repeated in the set 
C.remove("bat")
print(C)

# Remove vs Discard- Whether item is there or not discard will never throw an errow
# C.remove("rat")
C.discard("rat")
C.discard(4j)
print(C)
C.pop()
print(C)      #random deletion 