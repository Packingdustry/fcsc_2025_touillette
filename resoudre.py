encrypted = open("output.txt").read()

res = ['.'] * 64

for i in range(0, 32):
    res[i*2+1] = encrypted[i]

for i in range(32, 64):
    res[(i-32)*2] = encrypted[i]

print("".join(res))
