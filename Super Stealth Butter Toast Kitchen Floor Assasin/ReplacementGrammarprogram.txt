"""
Cameron Little
14 Jan 2014

Microsoft Code4Cash
"""

import re, math

f = open('ActualInput.txt', 'r')
f_str = f.read()
f.close()
lines = f_str.split('\r\n')
lines = [line for line in lines if line]

message = lines[-1]
rules = lines[:-1]

for rule in rules:
    rule_match = re.match("^(.+)\|(.+)$", rule)
    if rule_match:
        pattern = rule_match.group(1)
        replace = rule_match.group(2)

        message = message.replace(pattern, replace)

w = open('ReplacementGrammar.txt', 'w')
w.write(message + '\r\n')
w.close()

