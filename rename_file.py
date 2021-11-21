import re
import os
from alive_progress import alive_bar

def rename_files():
    multiple = input('do you want to scale multiple images? (y/n): ')
    if multiple == 'y':
        print('you are processing multiple images.')
        files_path = input('path to images: ')
        regex = r'.+[^/]'
        search = re.findall(regex, files_path)
        formatted_directory = search[0] + '/'
        files_path = formatted_directory
        #files_list = os.listdir(files_path)
        files_list = [f for f in os.listdir(files_path) if not f.startswith('.')]
        files_list.sort()
    else:
        print('you are processing a single image.')
        path = input('add full path to the image: ')
        files_path = os.path.dirname(path) 
        file_name=os.path.basename(path)
        files_list = []
        files_list.append(file_name)
        files_path = files_path+'/'

    new_basename = input('type the base name for your files: ')
    padding = input('specify the number of zeros(int) you want for file number padding: ')
    file_number = 0
    
    with alive_bar(len(files_list)) as bar:
        for file_name_extension in files_list:
            file_number = file_number +1
            padded_number = str((file_number)).zfill(int(padding))
            file_name = file_name_extension.rsplit('.', 1)[0]
            file_extension = file_name_extension.rsplit('.', 1)[1] 
            file_path = files_path + file_name_extension
            regex = r'.+[^/]'
            search = re.findall(regex, file_path)
            formatted_directory = search[0] + '/'
            new_filename = new_basename+'.'+padded_number+'.'+file_extension 
            print(file_name_extension)
            os.rename(files_path+file_name_extension, files_path+new_filename)
            bar()

if __name__ == "__main__":
    rename_files()