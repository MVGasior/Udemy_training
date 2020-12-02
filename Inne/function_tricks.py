def DoAction(action, parameter):
    print("action:", action)
    print("parameter:", parameter)
    return

DoAction('buy','shoes')

def DoAction2(action, *parameter):
    print("action:", action)
    print("parameter:", parameter)
    for element in parameter:
        print("element is",element)
    return

DoAction2('buy','shoes','socks')
DoAction2('buy','shoes','socks','t-shirt')

def DoAction3(action, what, **parameter):
    print("action:", action)
    print("what:", what)
    print("parameter:", parameter)
    for element in parameter:
        print(element,'=',parameter[element])
    return

DoAction3('buy','shoes',size=45,color='brown',type='sport')

def PrintAnimal(*animals):
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
    for animal in animals: 
        if animal == 'cat':
            print(txt_cat)
        elif animal == 'bear':
            print(txt_bear)
        elif animal == 'bat':
            print(txt_bat)
        else:
            print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)
            

    return

PrintAnimal('cat','bat','tiger')

from datetime import date

def LeftDayToTheEnd(*dates):
  

    for date_today in dates:

        date_and_year = date(date_today.year,12,31)
        delta = date_and_year - date_today
        print("Do sylwestra pozsotało:",delta.days,"od dnia",date_today)

    return

LeftDayToTheEnd(date(2020,8,23))
LeftDayToTheEnd(date(2020,9,1),date(2020,8,15),date(2020,11,21))
