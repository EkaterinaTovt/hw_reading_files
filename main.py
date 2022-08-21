import os, glob
from collections import Counter
PATH = os.getcwd()
pattern = '*.txt'
glob_path = os.path.join(PATH, pattern)
list_files = glob.glob(glob_path)
new_file = 'new_file.all'
if list_files:
    for file_name in list_files:
        with open(file_name, 'r') as fr, open (new_file, 'a') as fw:
            count_files = 0
            count = 0
            for file_name in fr:
                count_files += 1
            for line in fr:
                count += 1
                count_lines = sum(1 for line in fr)
                new_list_file = []
                new_list_count = []
                new_list_file.append(file_name)
                new_list_count.append(count_lines)
                new_list = list(zip(new_list_file, new_list_count))
                print(new_list.sort(key = lambda x: x[1]))
                print('Даны файлы: {file_name}\nСтрока номер {count} файла номер {count_files}')
                fw.write(f'{file_name}\n {count}\n Строка номер {count} файла номер {count_files}')
       

