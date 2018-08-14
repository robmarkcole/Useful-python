def add_offset(data, offset):
    return data['Random Number'] + offset

def analyse(data):
    data['Random Number + 2'] = add_offset(data, 2)
    return data