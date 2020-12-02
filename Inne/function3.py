from datetime import date
from datetime import timedelta



def GiveWorkingDay(year=date.today().year,\
                   month=date.today().month,\
                   day=date.today().day ):

    day = date(year,month,day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    return workingday

nextworkingday = GiveWorkingDay(2017,9,2)
print('Next working day after',201,9,2,'is',nextworkingday)
GiveWorkingDay()
print('Next working day after today is',nextworkingday)

print('Next working day after today is',GiveWorkingDay())

def PrintAnimal(animal):
    # this function prints a cat, bear or bat ascii-art
    txt_cat = r'''
|\---/|
| o_o |
 \_^_/'''
    txt_bear = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
    txt_bat = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/  
     '''
 
    if animal == 'cat':
        print(txt_cat)
        RightArg = 'True'
    elif animal == 'bear':
        print(txt_bear)
        RightArg = 'True'
    elif animal == 'bat':
        print(txt_bat)
        RightArg = 'True'
    else:
        RightArg = 'False'
        print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)
        
    return(RightArg)

print(PrintAnimal('cat'))
print(PrintAnimal('dog'))

def LeftDayToTheEnd(year,month,day):
    from datetime import date

    date_today = date(year,month,day)
    current_year = date_today.year
    date_and_year = date(current_year,12,31)
    delta = date_and_year - date_today

    return(delta.days)

print(LeftDayToTheEnd(2020,8,23))
