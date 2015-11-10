text = "ni talar bra latin"
print text[:]
print text[3:9]
print text[-5:]
print ''.join(reversed(text))
print {c: text.count(c) for c in list(set(text))}
print ''.join(set(sorted(text.replace(' ', ''))))

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print list(enumerate(seasons, start=1))

import calendar
print list(enumerate([calendar.month_name[i] for i in range(1, 13)], 1))
