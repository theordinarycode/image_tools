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
        local_settings['file_number'] = ''
        rename(global_settings, local_settings, file)

    
def rename(global_settings, local_settings, file):
    if(global_settings['multiple_files'] == True):
        os.rename(global_settings['path']+file, global_settings['output_directory'] + global_settings['basename'] + '.' + str(local_settings['file_number']) + '.' +  global_settings['file_extension'])
    else:
       os.rename(global_settings['path']+file, global_settings['output_directory'] + global_settings['basename'] + '.' +  global_settings['file_extension']) 

