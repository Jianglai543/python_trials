from operator import itemgetter
from itertools import groupby


row = [
    {'data':2013, 'mession':'abc'},
    {'data':2014, 'mession':'abcg'},
    {'data':2015, 'mession':'abcf'},
    {'data':2016, 'mession':'abce'},
    {'data':2014, 'mession':'abcd'}


]
# row.sort( key=itemgetter('data'))
row = sorted(row, key=itemgetter('data'))

for data, value in groupby(row, key=itemgetter('data')):
    print(data)
    for i in value:
        print('    ', i)