def GiveWorkingDay(year, month, day):
    #prints the nearest working day date
    from datetime import date
    from datetime import timedelta

    #day = date.today()
    day = date(year,month,day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print('working day for',day,'is',workingday)

    return


GiveWorkingDay(2017,9,30)




def LeftDayToTheEnd(year,month,day):
    from datetime import date

    date_today = date(year,month,day)
    current_year = date_today.year
    date_and_year = date(current_year,12,31)
    delta = date_and_year - date_today

    print(delta.days)
    return
 
LeftDayToTheEnd(2020,2,26)

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
    elif animal == 'bear':
        print(txt_bear)
    elif animal == 'bat':
        print(txt_bat)
    else:
        print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)
    
    return

PrintAnimal('dog')
