#Day1.py

#depths = [199,200,208,210,200,207,240,269,260,263]
depths=[]

f=open('Day01Input.txt','r')
lines = f.readlines()

for line in lines:
    depths.append(int(line))

increases = 0
for i in range (0,len(depths)-1):
    d1 = depths[i]
    d2 = depths[i+1]
    if d2 > d1:
        increases += 1

print(increases)