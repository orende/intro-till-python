text = "ni talar bra latin"
print text[:]
print text[3:9]
print text[-5:]
print ''.join(reversed(text))
print {c: text.count(c) for c in list(set(text))}
print ''.join(set(sorted(text.replace(' ', ''))))

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print list(enumerate(seasons, start=1))

from datetime import date
print list(enumerate([date(2015, i, 1).strftime('%B') for i in range(1,13)], 1))
