encrypted = open("output.txt").read()

res2 = ['.'] * 64

# Replacement des nombres décalés de 2 à la fin
for i in range(0, 32):
    res2[i*2+1] = encrypted[i]

for i in range(32, 64):
    res2[(i-32)*2] = encrypted[i]

# Replacement des nombres décalés de 8
res8 = ['']*8
print(res8)
for i in range(0, 64):
    for j in range(0, 8):
        print("j :", j, "i : ", i)
        if i%8==j:
            res8[j] += res2[i]

res8.reverse()
print(''.join(res8))
