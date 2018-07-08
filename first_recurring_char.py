#### 

def functn(l2):
    counts = {}
    for char in l2:
        if char in counts:
            return char
        else:
            counts[char] = 1
    return None

l2 = "MGHMCDMFD"
f2 = functn(l2)
print(f2)
