from os.path import exists
from HW7_CSV_creating import creating
from HW7_File_writing import writing_scv
from HW7_File_writing import writing_txt


path = 'HW7_Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()