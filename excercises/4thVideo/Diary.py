from datetime import datetime
import json
from pathlib import Path
import sys
file_name='File_pH'
def read_diary_entries(file_name):
        try:
            with open (file_name,'r',encoding='utf-8') as f:
                x=json.load(f)#To decode the object again
                return (x)  
        except json.decoder.JSONDecodeError:
             return {'entries':[]}
        except FileNotFoundError as FNF:
             return "File is not present"

while  not (Path(file_name).exists()):
    file_name=input("Enter the diary name: ")
    print(read_diary_entries(file_name))

diary_contents= read_diary_entries(file_name)
menu='0'
while menu !=3:
     print ("""Select Operation 
           1. Read Contents
           2. Write Contents
           3. Any other key to exit
           """)
     casing = input()
     try:
        casing=int(casing)
        if (casing ==1):
            print ("In 1st case")
            #print (diary_contents)
            for entry111 in diary_contents['entries']:
                 print (entry111['Timestamp'],entry111['Entry Text']) 
        elif (casing == 2):
            print ("In 2nd case")
            capture_user_contents=input()
            current_timestamp = datetime.now()
            human_readable_timestamp = current_timestamp.strftime('%Y-%m-%d %H:%M:%S')
            updated_contents= {'Timestamp':human_readable_timestamp,
                              'Entry Text': capture_user_contents}
            diary_contents['entries'].append(updated_contents)
            with open (file_name,'w') as f:
                json.dump(diary_contents,f)
        else:
            print("Exiting")
            sys.exit()  # This will exit the Python interpreter
     except ValueError as V:
          print("Caught Exiting")
          sys.exit()  # This will exit the Python interpreter
               
        





"""with open('Diary_entried.txt','w',encoding='utf-8') as f:
    current_timestamp = datetime.now()
    human_readable_timestamp = current_timestamp.strftime('%Y-%m-%d %H:%M:%S')
    f.write(human_readable_timestamp + "-->"+"My diary \n")"""