# This is a sample Python script.
my_dict={'Alex':1978, 'Max':1982, 'Roman':1976}
print(my_dict)
print(my_dict['Max'])
print('Not existing value:', my_dict.get('Peter'))
my_dict.update({'Oksana': 1978, 'Sveta': 1990})
print('Modified dict:', my_dict)
deleted=my_dict.pop('Max')
print('deleted value:', (deleted))

set_={'Alex', 25, 'Alex', 25, True, True}
print('Set:', set_)
set_.update({'Roman', 100, 'Roman', 100})
print('Modified set:', set_)