def regex_matching(s, p): 
    if len(p) == 0: 
        return (len(s) == 0) 
    if len(p) == 1 or p[1] != '*': 
        if (len(s) == 0 or (s[0] != p[0] and p[0] != '.')): 
            return False
        return regex_matching(s[1:], p[1:]) 
    if regex_matching(s, p[2:]): 
        return True
    i = 0
    while (i < len(s) and (s[i] == p[0] or p[0] == '.')): 
        if regex_matching(s[i + 1:], p[2:]): 
            return True
        i += 1
    return False
s = input("enter a variable")
p = input("enter a variable")
if (regex_matching(s, p)): 
    print("true") 
else: 
    print("false") 
