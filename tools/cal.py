import json

def load():
    with open('a.json', 'r') as f:
        return json.load(f)

a = load()
a = a.get('stat_status_pairs')

max_id = max([x['stat']['frontend_question_id'] for x in a])
notac = [x for x in a if x['status'] != 'ac']

locked = lambda a, l: len([x for x in a if x['paid_only'] and x['difficulty']['level'] == l])
unlocked = lambda a, l: len([x for x in a if not x['paid_only'] and x['difficulty']['level'] == l])

e = locked(notac, 1)
m = locked(notac, 2)
h = locked(notac, 3)

un_e = unlocked(notac, 1)
un_m = unlocked(notac, 2)
un_h = unlocked(notac, 3)

count = e+m+h
res = ''
res += '<=%d  e=%d+%d  m=%d+%d  h=%d+%d  %d=%d+%d' % (max_id, e, un_e, m, un_m, h, un_h, len(a), count, len(a)-count)
res += '  %d=%d+%d' % (len(a)-count, len(a)-len(notac), len(notac)-count)
print res
# command to copy output: pbcopy  pbpaste
