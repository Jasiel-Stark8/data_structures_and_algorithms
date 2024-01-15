"""Marvel List/Array manipulation"""

# 0 Assign List
heros = ['spider man' , 'thor' , 'hulk' , 'iron man' , 'captain america']

# 1 Length of list
print(len(heros))

# 3 append black panther
if 'black oanther' in heros:
    heros.remove('black panther')
heros.insert(3, 'black panther')
print(heros)

# 4 remove thor and hulk then repalce them witth doctor strange in one line
heros[1:3] = ['doctor strange']
print(heros)

# 5
print(dir(heros))
print(sorted(heros))
