def WeekDayInFranch(dayNumber) :

    names = {
        0: "lundi",
        1: "mardi",
        2: "mercredi",
        3: "jeudi",
        4: "vendredi",
        5: "samedi",
        6: "dimanche"
        }

    return names.get(dayNumber,"error")

print(WeekDayInFranch(4))
        
def GiveGeomSeqElement(a1 = 2,factor = 2,index =2):

    value = a1*pow(factor,index-1)
    return value

print(GiveGeomSeqElement(1,2,64))
print('---------------------------------------------------')

a1 = 3
factor = 2
maxindex = 10

for i in range(1,maxindex):             #Tu istotne, nie podajemy jednego parametru po in tylko cały zakres
    an = GiveGeomSeqElement(a1=a1,factor=factor,index=i)
    print('Term',i,'=',an)
print('----------------------------------------------------')


def GiveFactorForGeomSeq(term,nextterm):

    factor = nextterm / term
    return factor

print(GiveFactorForGeomSeq(12,24))
print('-----------------------------------------------------')

def GiveSumOfNElementsGeomSeq(a1 = 2,factor = 2, n =2):

    suma = a1*(1-pow(factor,n))/(1-factor)
    return suma

print(GiveSumOfNElementsGeomSeq(2,3,4))
print('------------------------------------------------------')
