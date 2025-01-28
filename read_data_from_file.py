def read_data(file_name='data.txt'):
    data_lst = []
    file = open(file_name, 'r')
    while True:
        content=file.readline()
        if not content:
            break
        data_lst.append(eval(content))
    file.close()
    return data_lst

def get_data_types(data):
    data_type = {}
    data_first = data[0]
    data_keys = [x for x in data_first.keys()]
    for d in data_keys:
        if type(data_first[d]) is type('str'):
            data_type[d] = d + " VARCHAR(15)"
        elif type(data_first[d]) is type(1.0):
            data_type[d] = d + " FLOAT"
        else:
            data_type[d] = d + " INT"
    return data_type

if __name__ == '__main__':
    datas = read_data('data.txt')
    data_types = get_data_types(datas)
        
    print(data_types)
            