d = {1:2, 2:'123'}
m = list(d.keys())[0]
for i in d.keys():
    if i > m:
        m = i
print(d.get(m))

