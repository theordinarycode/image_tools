import os 
import re

def get_path():
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
        print('Do you want to set a basename for the output files?')
        rename = input('type yes or no: ')
        if rename.lower() in ['yes', 'y']:
            settings['basename'] =input('Basename: ')
        else: 
           settings['basename'] = ''
    else:
        settings['multiple_files'] = False
        path = input('Full path to your image (including the image): ')
        settings['path'] = os.path.dirname(path)+'/'
        print('Do you want to rename your file?')
        rename = input('Type yes or no: ')
        settings['basename']=os.path.basename(path).split('.')[0]

    return settings

def process(settings):
    if(settings['multiple_files'] == True):
        for file in os.listdir(settings['path']):
            if not file.startswith('.'):
                print(file)
    else:
        print('ok its a single file')


if __name__ == "__main__":
    settings = get_path()
    print(settings)
    process(settings)