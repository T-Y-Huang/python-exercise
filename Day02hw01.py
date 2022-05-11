s = 'This company is not poor at all.'

# not_index
n_index = s.index('not')

# l_index
l_index = s.index('at all') + 5

rep = s[n_index:l_index+1]
print(s.replace(rep, 'good'))
