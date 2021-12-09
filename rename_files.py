import re
import os
from alive_progress import alive_bar

def get_local_settings(settings):
    local_settings = {}
    local_settings['file_number'] = 0
    return local_settings

def rename_files(global_settings):
    if(global_settings['multiple_files'] == True):
        local_settings = get_local_settings(global_settings)
        num = 0
        files_list = os.listdir(global_settings['path'])
        with alive_bar(len(files_list)) as bar:
            for file in files_list:
                if not file.startswith('.'):
                    local_settings['file_number'] = str((num)).zfill(int(4))
                    num = num +1
                    rename(global_settings, local_settings, file)
                bar()
    else:
        local_settings = get_local_settings(global_settings)
        file = global_settings['filename']
        rename(global_settings, local_settings, file)

    
def rename(global_settings, local_settings, file):
    os.rename(global_settings['path']+file, global_settings['output_directory'] + global_settings['basename'] + '.' + local_settings['file_number'] + '.' +  global_settings['file_extension'])




    # multiple = input('do you want to rename multiple images? (y/n): ')
    # if multiple == 'y':
    #     print('you are processing multiple images.')
    #     files_path = input('path to images: ')
    #     regex = r'.+[^/]'
    #     search = re.findall(regex, files_path)
    #     formatted_directory = search[0] + '/'
    #     files_path = formatted_directory
    #     files_list = [f for f in os.listdir(files_path) if not f.startswith('.')]
    #     files_list.sort()
    # else:
    #     print('you are processing a single image.')
    #     path = input('add full path to the image: ')
    #     files_path = os.path.dirname(path) 
    #     file_name=os.path.basename(path)
    #     files_list = []
    #     files_list.append(file_name)
    #     files_path = files_path+'/'


    # new_basename = input('type the base name for your files: ')
    # padding = input('specify the number of zeros(int) you want for file number padding: ')
    # file_number = 0


