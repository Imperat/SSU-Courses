import random


class Part(object):

    @staticmethod
    def get_res(k):
        return random.random() > 0.1

count_good = 0
count_repa = 0
count_badd = 0

for i in range(1000):
    isd = map(Part().get_res, range(4))
    kefl = 0
    for r in isd:
        if r == False:
            kefl += 1
    if kefl == 0:
        count_good += 1
    if kefl == 1:
        count_repa += 1
    if kefl >= 2:
        count_badd += 1

print 'GOOD: %s ' % (count_good / 1000.0)
print 'BAD: %s  ' % (count_badd / 1000.0)
print 'REPA: %s ' % (count_repa / 1000.0)
