def write_data(str='',file_name='report.txt'):
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(f'{str}\n')
        
if __name__ == '__main__':
    str= ''
    write_data_to_file(str)