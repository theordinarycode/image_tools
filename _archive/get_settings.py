import os 
import re

settings = {}

def get_settings():
    print('Will you be processing multiple images?')
    multiple = input('Type yes or no: ')
    print('Please indicate the operations you\'d like to perform...')
    commands = input('Type any combination of the following commands: rename, resize, add_metadata, combine_images. Each command should separated by a comma (ex: one,two,three).  \nOperations: ')
    commandsList = commands.split(',')
    settings['commands'] = commandsList
    
    if multiple.lower() in ['yes', 'y'] :
        settings['multiple_files'] = True
        path = input('Path to your images: ')
        regex = r'.+[^/]'
        search = re.findall(regex, path)
        formatted_directory = search[0] + '/'
        settings['path'] = formatted_directory 
        settings['number_of_files'] = len(os.listdir(path))

        first_pass = True
        for file in os.listdir(settings['path']):
            if not file.startswith('.') and first_pass == True:
                first_image = file 
                settings['file_extension']=first_image.split(".")[-1]
                #print(os.path.basename(first_image).split('.')[0])
                settings['basename'] = os.path.basename(first_image).split('.')[0]
                if 'rename' in settings['commands']:
                    rename = 'yes'
                else:
                    rename = 'no'
                if rename.lower() in ['yes', 'y']:
                    settings['basename'] =input('New File Name: ')
                first_pass = False

    else:
        settings['multiple_files'] = False
        path = input('Full path to your image (including the image): ')
        settings['path'] = os.path.dirname(path)+'/'
        #print('Do you want to rename your file?')
        settings['filename']=os.path.basename(path)
        #rename = input('Type yes or no: ')
        if 'rename' in settings['commands']:
            rename = 'yes'
        else:
            rename = 'no'
        if rename.lower() in ['yes', 'y']:
            settings['basename'] =input('New file name: ')
        else:
            settings['basename']=os.path.basename(path).split('.')[0]
        settings['file_extension']=os.path.basename(path).split(".")[-1]
        settings['number_of_files'] = 1

    #output_directory = input('output directory: ')
    output_directory = settings['path']
    regex = r'.+[^/]'
    search = re.findall(regex, output_directory)
    formatted_directory = search[0] + '/'
    settings['output_directory'] = formatted_directory
    
    return settings