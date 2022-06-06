st = "HeLlO WoRlD"
upper = 0
lower = 0
for i in st:
    if i == " ":
        continue
    elif i == i.upper():
        upper = upper+1
    else:
        lower = lower+1

print(upper)
print(lower)