"""
This module generates all the links in a given MOSS result URL,
to facilitate cloning the result. The links are written to a text file,
the name of which can be configured by modifying FILE_NAME.
"""

LAST_MATCH = 249
ID = 702110361
FILE_NAME = 'all_links'

assert LAST_MATCH <= 1000, f'Are you sure you have {LAST_MATCH} matches?'
lst = [f'http://moss.stanford.edu/results/{ID}/']
for i in range(0, LAST_MATCH + 1):
    lst.append(f'http://moss.stanford.edu/results/{ID}/match{i}.html')
    lst.append(f'http://moss.stanford.edu/results/{ID}/match{i}-top.html')
    lst.append(f'http://moss.stanford.edu/results/{ID}/match{i}-0.html')
    lst.append(f'http://moss.stanford.edu/results/{ID}/match{i}-1.html')

with open(f'{FILE_NAME}.txt', 'w') as file:
    file.write('\n'.join(lst))
