
school = [3,1,4,2,1,1,1,1,1,1,1,4,1,4,1,2,1,1,2,1,3,4,5,1,1,4,1,3,3,1,1,1,1,3,3,1,3,3,1,5,5,1,1,3,1,1,2,1,1,1,3,1,4,3,2,1,4,3,3,1,1,1,1,5,1,4,1,1,1,4,1,4,4,1,5,1,1,4,5,1,1,2,1,1,1,4,1,2,1,1,1,1,1,1,5,1,3,1,1,4,4,1,1,5,1,2,1,1,1,1,5,1,3,1,1,1,2,2,1,4,1,3,1,4,1,2,1,1,1,1,1,3,2,5,4,4,1,3,2,1,4,1,3,1,1,1,2,1,1,5,1,2,1,1,1,2,1,4,3,1,1,1,4,1,1,1,1,1,2,2,1,1,5,1,1,3,1,2,5,5,1,4,1,1,1,1,1,2,1,1,1,1,4,5,1,1,1,1,1,1,1,1,1,3,4,4,1,1,4,1,3,4,1,5,4,2,5,1,2,1,1,1,1,1,1,4,3,2,1,1,3,2,5,2,5,5,1,3,1,2,1,1,1,1,1,1,1,1,1,3,1,1,1,3,1,4,1,4,2,1,3,4,1,1,1,2,3,1,1,1,4,1,2,5,1,2,1,5,1,1,2,1,2,1,1,1,1,4,3,4,1,5,5,4,1,1,5,2,1,3]
#school=[3,4,3,1,2]
days = 80 

def numCommas(number):
    return '{:,}'.format(number)

def processSchool(days,oldschool):
    while days > 0 :
        newschool = []
        fry = []
        for fish in oldschool:
            fish -= 1
            if fish > -1:
                newschool.append(fish)
            else:
                newschool.append(6)
                fry.append(8)
        days -= 1
        oldschool = newschool + fry
    return(len(oldschool))

print('initial school of fish',len(school))

print('in ',days,' days . . . ')
lookup = {}
for i in range(1,max(school)+1):
    lookup[i] = processSchool(days,[i])
    print('fish ',i,' will become ',lookup[i], 'fish!')
    
total = 0
for fish in school:
    total += lookup[fish]
    
print(total)

    

