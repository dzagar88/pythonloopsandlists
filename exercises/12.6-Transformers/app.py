incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

#Your code go here:


def data_transformer(data):
    return list(map(lambda x: x['name'] + ' ' + x['last_name'], data))
    
full_names = data_transformer(incoming_ajax_data)
print(full_names)


# using an f-string: return list(map(lambda x: f"{x['name']} {x['last_name']}", data))
