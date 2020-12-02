##persons=['Elizabeth','Steven','Sebastian','Margaret','Svetlana','Raphael']
##
##domain = 'mycompany.com'
##
##for person in persons:
##    email = person + '@' + domain
##    print('Email for\t', person, '\tis\t', email)
##else:
##    print('--end of the list--')

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Interner connection lost',
        'Error:Access denied']

for dat in data:
    print(dat.upper())

for s in data:
    elements = s.split(':')
    if elements[0] == 'Error':
        print(elements[0].upper(),elements[1].upper())
    else:
        print(elements[0].upper(),elements[1])
        


