s="A Python script"
print(s[0])
print(s[2])
print(s[2:7])  #od 2 do 7
print(s[:8])
print(s[8:])
print(s[222:999])


message = 'Document "cv.doc" was printed on printer: XEROX'
print(message.find(':'))

print(message[(message.find(':')+2):])

print(message[(message.find('"')+1):])
tmp = message[(message.find('"')+1):]
print(tmp[:(tmp.find('"'))])

q = "THE EYES"
print(q[0]+q[1]+q[2]+q[5]+q[3]+q[7]+q[4]+q[6])

q = "a gentleman"
print(q[3]+q[6]+q[7]+q[2]+q[0]+q[4]+q[5]+q[1]+q[8:])

o = "THE MORSE CODE"
print(o[1:3]+o[6]+o[8:12]+o[4]+o[2:4]+o[12]+o[11]+o[0]+o[7])

line = "'Program \"Kropka nad i\" nadamy o: 22:00"
print(line)
time = line[line.find(':')+1:]
print(time)
tmp = line[line.find('"')+2:]
title = tmp[:tmp.find('"')]
print(title)
print(title + time)

linia = "'Program \"Pytanie na śniadanie\" nadamy o : 6:00\'"
print(linia)
tmpczas = linia[linia.find(':')+2:]
czas = tmpczas[:tmpczas.find("'")]
print(czas) 
tmptytul = linia[linia.find('"')+1:]
tytul = tmptytul[:tmptytul.find('"')]
print(tytul)
print(tytul,czas)
