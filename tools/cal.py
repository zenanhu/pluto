import json

def load():
    with open('a.json', 'r') as f:
        return json.load(f)

a = load()
a = a.get('stat_status_pairs')
max_id = max([x['stat']['frontend_question_id'] for x in a])
notac = [x for x in a if x['status'] != 'ac']

locked = lambda a, l: len([x for x in a if x['paid_only'] and x['difficulty']['level'] == l])

e = locked(notac, 1)
m = locked(notac, 2)
h = locked(notac, 3)
count = e+m+h
print '<=%d  e: %d  m: %d  h: %d  %d  %d %d' % (max_id, e, m, h, count, len(a), len(a)-count)
print '%d %d' % (len(a)-len(notac), len(notac)-count)
# command to copy output: pbcopy  pbpaste
