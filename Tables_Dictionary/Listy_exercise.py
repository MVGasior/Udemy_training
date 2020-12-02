hitsTitles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
additional = ['CHILD IN TIME','AGAIN']
hitsTitles.extend(additional)

hitsTitles.insert(2,'HOTEL CALIFORNIA')

hitsTitles.insert(0,'THE SOUND OF SILENCE')
print(hitsTitles.index('HOTEL CALIFORNIA'))

hitsTitles.remove('HOTEL CALIFORNIA')

hitsTitles.remove('THE SOUND OF SILENCE')
hitsTitles.insert(0,'ENJOY THE SILENCE')

hitsToRead = hitsTitles.copy()
hitsToRead.sort()

print(hitsToRead.pop(0))
print(hitsToRead.pop(0))

additionalSongs =['NOTHING COMPARES 2 U','WISH YOU WERE HERE']
hitsToRead.extend(additionalSongs)
print(hitsToRead.count('NOTHING COMPARES 2 U'))
print(hitsToRead.count('WISH YOU WERE HERE'))
      

hitsToRead.clear()

print(hitsTitles)
print(hitsToRead)
print(additionalSongs)


CountriesIWantVisit = ['Argentina','Italy','Georgia','Japan','Chille','Canada']
CountriesIWantVisit.sort()
CountriesAgaWantVisit = ['Peru','USA','New Zeland']

CountriesWeWantVisit = CountriesIWantVisit.copy()

CountriesWeWantVisit.sort()
print(CountriesWeWantVisit.index('Georgia'))
print(CountriesWeWantVisit.pop(3))

CountriesWeWantVisit.extend(CountriesAgaWantVisit)
print(CountriesWeWantVisit.index('Chille'))
print(CountriesWeWantVisit.pop(2))
CountriesWeWantVisit.sort()




print(CountriesIWantVisit)
print(CountriesAgaWantVisit)
print(CountriesWeWantVisit)



