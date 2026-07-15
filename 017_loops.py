# 1 While loop
i = 1
while i <= 50:
    print(i)
    i+=1

# 2 For loop
for i in range(0, 7): #range(7) will also work
    print(i)

#Break statement
for i in range(10):
    if i == 5:
        break #it stops the program when the condition is met
    print(i)

#Continue statement
for i in range(10):
    if i == 5:
        continue #it skips the current iteration and moves to the next iteration
    print(i)

#Pass statement
for i in range(10):
    if i == 5:
        pass #it does nothing, it is just a placeholder
    print(i)