import re
#names
file_path = "MOCK_DATA.txt"
names_file_path = "names.txt"

file_reader = open(file_path, mode="r", encoding="Latin-1")
final_names = open(names_file_path, mode="w", encoding="Latin-1")

class_txt = file_reader.read()

searcher = r'[A-Z]+[A-z]+\w+\s+[A-z]+[a-z]+\w+'
results_all = re.findall(searcher, class_txt)

for item in results_all:
    final_names.write(item + '\n')
print(f'Total:{str(len(results_all))}')

# mail
file_path1 = "MOCK_DATA.txt"
mails_file_path1 = "mails.txt"

file_reader1 = open(file_path1, mode="r", encoding="Latin-1")
final_mails1 = open(mails_file_path1, mode="w", encoding="Latin-1")

class_txt1 = file_reader1.read()

searcher1 = r'\w+@\w+.[a-z]+'
results_all = re.findall(searcher1, class_txt1)

for item in results_all:
    final_mails1.write(item + '\n')
print(f'Total:{str(len(results_all))}')

# formats
file_path2 = "MOCK_DATA.txt"
format_file_path2 = "formats.txt"

file_reader2 = open(file_path2, mode="r", encoding="Latin-1")
final_files2 = open(format_file_path2, mode="w", encoding="Latin-1")

class_txt2 = file_reader2.read()

searcher2 = r"[A-Z]+[a-z]+\w+[.]+[a-z]+[0-9]|[A-Z]+[a-z]+\w+[.]+[a-z]+|[A-Z]+[a-z]+[.]+[a-z]+" \
     r"[0-9]|[A-Z]+[a-z]+[.]+[a-z]+|[A-Z]+[a-z]+[.]+[a-z]+|[A-Z]+[.]+[a-z]+|[A-Z]+[.]+[a-z]+[0-9]" \

results_all = re.findall(searcher2, class_txt2)

for item in results_all:
    final_files2.write(item + '\n')
print(f'Total:{str(len(results_all))}')

# ides
file_path3 = "MOCK_DATA.txt"
id_file_path3 = "ides.txt"

file_reader3 = open(file_path3, mode="r", encoding="Latin-1")
final_ides3 = open(id_file_path3, mode="w", encoding="Latin-1")

class_txt3 = file_reader3.read()

searcher3 = r'#\w+'
results_all = re.findall(searcher3, class_txt3)

for item in results_all:
    final_ides3.write(item + '\n')
print(f'Total:{str(len(results_all))}')