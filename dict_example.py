# person1= {'ID': 1, 'name': "Ankan", 'email': "1001193@daffodil.ac" }
# person2= {'ID': 2, 'name': "Parvez", 'email': "1001190@daffodil.ac" }
# person3= {'ID': 3, 'name': "Muntakim", 'email': "1001197@daffodil.ac" }
# person4= {'ID': 4, 'name': "Rajjo", 'email': "1001193@daffodil.ac" }
# person5= {'ID': 5, 'name': "Parvez", 'email': "1001190@daffodil.ac" }
# person6= {'ID': 6, 'name': "Muntakim", 'email': "1001197@daffodil.ac" }

perlist=[
    {'ID': 1, 'name': "Ankan", 'email': "1001193@daffodil.ac" },
    {'ID': 2, 'name': "Parvez", 'email': "1001190@daffodil.ac" },
    {'ID': 3, 'name': "Muntakim", 'email': "1001197@daffodil.ac" },
    {'ID': 4, 'name': "Rajjo", 'email': "1001193@daffodil.ac" },
    {'ID': 5, 'name': "Parvez", 'email': "1001190@daffodil.ac" },
    {'ID': 6, 'name': "Muntakim", 'email': "1001197@daffodil.ac" }
]

print('%-5s %-30s %-20s' % ('ID','Person Name','Email'))
print('='*80)
for per in perlist:
    print('%-5s %-30s %-20s' % (per['ID'],per['name'],per['email']))