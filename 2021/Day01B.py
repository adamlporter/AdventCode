#Day1.py

#depths = [199,200,208,210,200,207,240,269,260,263]
depths = []

f=open('Day01Input.txt','r')
lines = f.readlines()

for line in lines:
    depths.append(int(line))

increases = 0
for i in range (0,len(depths)-3):
    d1 = depths[i]
    d2 = depths[i+1]
    d3 = depths[i+2]
    d4 = depths[i+3]
    
    if d1 < d4:
        increases += 1

print(increases)