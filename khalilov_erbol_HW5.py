import re

file_path = "MOCK_DATA.txt"
names_file_path = "names.txt"
mails_file_path = "mails.txt"
format_file_path = "formats.txt"
id_file_path = "ides.txt"

file_reader = open(file_path, mode="r", encoding="Latin-1")
final_names = open(names_file_path, mode="w", encoding="Latin-1")
final_mails = open(mails_file_path, mode="w", encoding="Latin-1")
final_formats = open(format_file_path, mode="w", encoding="Latin-1")
final_files = open(id_file_path, mode="w", encoding="Latin-1")

class_txt = file_reader.read()

searcher = r"[a-z]+@\w+.\w+.+"
results_all = re.findall(searcher, class_txt)

for item in results_all:
    print(item)
    final_mails.write(item + "\n")
print(f"Totals: {str(len(results_all))}")