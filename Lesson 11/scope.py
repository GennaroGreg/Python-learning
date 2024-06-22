name = "Greg" # Global Scope - available to entire file
count = 1

def greeting(name):
    color = "Red" # Local Scope - available to function
    print(color)
    print(name)

greeting("Cody")

def another():
    greeting("Percy")
    global count # Can't modify global value in local scope without calling Global      
    count += 1
    print(count)

another()

