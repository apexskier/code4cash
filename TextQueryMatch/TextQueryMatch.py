"""
Cameron Little
14 Jan 2014

Microsoft Code4Cash
"""

import re, math

f = open('SampleInput.txt', 'r')
f_str = f.read()
f.close()
lines = f_str.split('\r\n')

num_queries = lines[0]
lines = lines[1:]
pairs = [[lines[i], lines[i + 1]] for i in range (0, len(lines), 2)]
print num_queries
print lines
count = 0
results = []

def test(query, body):
    query = query.lower()
    body = body.lower()
    for char in

    return False

for pair in pairs:
    result = test(pair[0], pair[1])
    if result:
        count += 1
        results.append('true')
    else:
        results.append('false')

print results

w = open('TextQueryMatch.txt', 'w')
w.write(str(count) + '\r\n' + '\r\n'.join(results) + '\r\n')
w.close()

