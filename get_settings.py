import os 
import re

def get_settings():
    print('Will you be processing multiple images?')
    multiple = input('Type yes or no: ')
    settings = {}
    if multiple.lower() in ['yes', 'y'] :
        settings['multiple_files'] = True
        path = input('Path to your images: ')
        regex = r'.+[^/]'
        search = re.findall(regex, path)
        formatted_directory = search[0] + '/'
        settings['path'] = formatted_directory 
        settings['number_of_files'] = len(os.listdir(path))
        print('Do you want to set a basename for the output files?')
        rename = input('type yes or no: ')
        if rename.lower() in ['yes', 'y']:
            settings['basename'] =input('Basename: ')
        else:
            first_pass = True
            for file in os.listdir(settings['path']):
                if not file.startswith('.') and first_pass == True:
                    first_image = file
                    #print(os.path.basename(first_image).split('.')[0])
                    first_pass = False
            settings['basename'] = os.path.basename(first_image).split('.')[0]
    

    else:
        settings['multiple_files'] = False
        path = input('Full path to your image (including the image): ')
        settings['path'] = os.path.dirname(path)+'/'
        print('Do you want to rename your file?')
        settings['filename']=os.path.basename(path)
        rename = input('Type yes or no: ')
        if rename.lower() in ['yes', 'y']:
            settings['basename'] =input('Basename: ') 
        else:
            settings['basename']=os.path.basename(path).split('.')[0]
        settings['file_extension']=os.path.basename(path).split(".")[-1]

    output_directory = input('output directory: ')
    settings['output_directory'] = output_directory
    
    return settings