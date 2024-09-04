# File Handling- the key function to work with the file is open(), The open() function takes 2 parameters (file name, mode)
# mode means- what we want to do with the file
# Read("r"), Write("w"), Append("a"), and Create("x")

#To read a file 
a=open("C:\\Users\\ftska\\Music\\Encodes\\sample_project_2\\YHills\\sample-1.txt", "r")
print(a.read(150))   # 150 characters
# OR
b=open(r"C:\Users\ftska\Music\Encodes\sample_project_2\YHills\sample-1.txt")
print(b)
# OR
c=open("C:\\Users\\ftska\\Music\\Encodes\\sample_project_2\\YHills\\sample-1.txt")
print(c.readline(5))
# OR
d=open("C:\\Users\\ftska\\Music\\Encodes\\sample_project_2\\YHills\\sample-1.txt")
print(d.readline(1))
print(d.readline(1))
print(d.readline(1))
d.close()
# print(d.readline(1))  #file is closed

e=open(r"C:\Users\ftska\Music\Encodes\sample_project_2\YHills\sample-1.txt", "a")
e.write("Mumma is the best\n")
e.close()
e=open(r"C:\Users\ftska\Music\Encodes\sample_project_2\YHills\sample-1.txt", "r")
print(e.read())
#Write() will overwrite the existing content, append() will add the content to the last
f=open("C:\\Users\\ftska\\Music\\Encodes\\sample_project_2\\YHills\\sample-1.txt", "w")
f.write("She is very nice.")
f.close()
f=open("C:\\Users\\ftska\\Music\\Encodes\\sample_project_2\\YHills\\sample-1.txt", "r")
print(f.read())

#Create()
# h=open("firstfile.txt", "x")
# h=open(r"C:\Users\ftska\Music\Encodes\sample_project_2\firstfile.txt", "w")
# h.write("He is very nice.")
# h.close()
# h=open(r"C:\Users\ftska\Music\Encodes\sample_project_2\firstfile.txt", "r")
# print(h.read())

#Loops and Conditionals in python-ifelse, for
Weather="Windy" 
if Weather=="Sunny":   # ==(comparision operator) for comaparision
    print("we'll go out 50kms")
elif Weather=="Cloudy":
    print("We'll go out 4kms")
elif Weather=="Windy":
    print("We'll go out 20kms")       
else:
    print("no")    
    
# for-to iterate over a sequence(list, tuple, set, string) again and again
w={"Kanika", "Rajeev", "Mamta", "Beenu"}     # Sequence-Set
for i in w:
    print(i)    # i-temporary variable
k=("Vinit", "Pinky", "Shona", "Babu")     #Sequence-Tuple
for i in k:
    print(i)    
j="Girl"
for i in j:
    print(i)
h="Kan ika" 
for i in h:
    print(i)

A=input("How is she")
if A==("good"):
    print("happy fo her")    
else:
    print("will ask her")    # this code will run via running python file not the code. Run code and runnning python compiling differs.

# while-a while loop in python is a control statement that allows code to be executed repeatedly based on the given condition. 
#      -The loop continues executing until or unless condition gets false. 
r=7
sum=0
i=1
while i<=r:
    sum+=i
    i=i+1 
print(sum)    

i=1
while i<6:
    print(i)      
    i=i+1            
    i=i+3        # final snippet will execute 

i=1
while i<5:
    print(i)
    if i==2:
        break
    i=i+1        

# i=1
# while i<9:
#     print(i)
#     if i==5:
#         continue               # skips everything after 5 and an infinite loop of 5 will be there.
#     i=i+1    
# The error in the code is due to the continue statement inside the if block. When i is equal to 5, 
# the continue statement skips the rest of the code within the loop, including the increment of i. As a result,
# i remains 5, causing an infinite loop where i is always 5 and never increments, leading to a never-ending loop.

i=1
while i<10:
    i=i+1
    if i==5:
        continue
    print(i)     # 1 will not be print as 1 is 1 that is 2, printing will start from 2

i=0
while i<11:
    i=i+1
    if i==4:
        continue
    if i==8:
        continue
    print(i)     # we can't do if i==4 and i==8 as a single statement because that means i has 2 values at the same time.

i=15
j=10
sum=i+j
while sum<50:
    i+=1
    j+=1
    if i==20:
        break
print(sum)    

    