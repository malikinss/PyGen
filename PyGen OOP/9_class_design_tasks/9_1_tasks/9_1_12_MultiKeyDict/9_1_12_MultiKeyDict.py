'''
TODO:
    Implement a MultiKeyDict class that is almost identical to the dict class.

    Creating an instance of the MultiKeyDict class should be similar
    to creating an instance of the dict class:
        multikeydict1 = MultiKeyDict(x=1, y=2, z=3)
        multikeydict2 = MultiKeyDict([('x', 1), ('y', 2), ('z', 3)])
        print(multikeydict1['x']) # 1
        print(multikeydict2['z']) # 3

    A special feature of the MultiKeyDict class should be the alias() method,
    which should allow you to give aliases to existing keys.

    Access by the created alias should not differ in any way from access by
    the original key, i.e. from the moment the alias is created the value has
    two keys (or more, if there are several aliases):
        multikeydict = MultiKeyDict(x=100, y=[10, 20])
        multikeydict.alias('x', 'z') # adding alias 'z' to key 'x'
        multikeydict.alias('x', 't') # adding alias 't' to key 'x'
        print(multikeydict['z']) # 100
        multikeydict['t'] += 1
        print(multikeydict['x']) # 101
        multikeydict.alias('y', 'z') # now 'z' becomes an alias of key 'y'
        multikeydict['z'] += [30]
        print(multikeydict['y']) # [10, 20, 30]

    The value must remain accessible via the alias even if the original key
    has been deleted:
        multikeydict = MultiKeyDict(x=100)
        multikeydict.alias('x', 'z')
        del multikeydict['x']
        print(multikeydict['z']) # 100

    Keys must take precedence over aliases.

    If some key and alias are the same, then all operations on them must be
    performed with the key:
        multikeydict = MultiKeyDict(x=100, y=[10, 20])
        multikeydict.alias('x', 'y')
        print(multikeydict['y']) # [10, 20]
'''
