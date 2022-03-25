import os
import re


my_path = my_path = 'Your Path'
os.chdir(my_path)

for branch , folder, files in os.walk("extracted_content"):
    
    print("Folder: " + branch)
    
    for subfolder in folder:
        print("Subfolder: " + subfolder)
    
    for document in files:
        file_path = os.getcwd() + '\\' + branch + '\\' + document
        with open(file_path) as doc:
            text = doc.read()
            match = re.search(r'\d{3}-\d{3}-\d{4}', text)
            if match != None:
                text_found = match
   
        print('Searched: ' + file_path)
            
    print('\n')
print("Match Found")
print(text_found)        
        