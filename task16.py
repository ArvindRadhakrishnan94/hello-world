  GNU nano 2.5.3              File: task15.py                                   

def invert_dict():
        d = {'name': 'Luke', 'age': 43, 'friend': 'Joe'}
        print(d, id(d))

# Invert d
        t = {v: k for k, v in d.items()}

# Copy t to d
        d.clear()
        d.update(t)
# Remove t
        del t
        print(d, id(d))
invert_dict()

