Tax = (4, 7, 8, 23)

print(Tax[-1])
print(Tax.index(7))
print(Tax.count(8))
print(max(Tax))

TaxList = list(Tax)
TaxList.append(30)
NewTax = tuple(TaxList)

print(Tax)
print(TaxList)
print(NewTax)

(tax1,tax2,tax3,tax4) = Tax
print(tax1,tax2,tax3,tax4)

a=1
b=10


marketing = ['loyality program','client promotion','market research']
print(marketing)

marketing.append('public relations')
print(marketing)
print(marketing[3])
marketing.insert(2,'investor relations')
print(marketing)
emailMarketing = marketing.copy()
emailMarketing.sort()
print(emailMarketing)

internalEmails = ['internal communication']

emailMarketing.extend(internalEmails)
print(emailMarketing)

email = tuple(emailMarketing)
print(email)
