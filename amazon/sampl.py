a="Hello"

for i, var in enumerate(a):
    if i + 1 == len(a):
        special_function(var)
    else:
        not_so_special_function(var)
