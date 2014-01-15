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
w = open('NDrome.txt', 'w')

def test_chunks(n_chunks):
    to_match_num = int(math.ceil(len(n_chunks) / 2))

    l = len(n_chunks) - 1
    for i in range(to_match_num):
        if n_chunks[i] != n_chunks[l - i]:
            return False

    return True

for line in lines:
    line_match = re.match("^(.+)\|(\d+)$", line)
    if line_match:
        text = line_match.group(1)
        n = int(line_match.group(2))
        n_chunks = [text[i:i+n] for i in range(0, len(text), n)]

        w.write(line + '|' + str(1 if test_chunks(n_chunks) else 0) + '\r\n')

w.close()
