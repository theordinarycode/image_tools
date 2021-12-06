#simple python script to resize images
import re
import os
from PIL import Image
from alive_progress import alive_bar

FORMATS = {
    'PNG': 'png',
    'JPEG': 'jpg',
    'GIF': 'gif'
}

FILTERS = {
    'hard' : Image.NEAREST,
    'soft' : Image.BICUBIC
}

resampling = Image.NEAREST

def get_extension(format):
    return FORMATS.get(format, 'default')

def get_filter(filter):
    return FILTERS.get(filter, 'default') 

def get_current_filepath(path):
    return path

def resize_images(global_settings):
    
    if(global_settings['multiple_files'] == True):
        local_settings = get_local_settings(global_settings)
        num = 0
        files_list = os.listdir(global_settings['path'])
        with alive_bar(len(files_list)) as bar:
            for file in files_list:
                if not file.startswith('.'):
                    local_settings['file_number'] = str((num)).zfill(int(4))
                    num = num +1
                    resize(global_settings, local_settings, file)
                bar()
    else:
        local_settings = get_local_settings(global_settings)
        print(global_settings)
        file = global_settings['filename']
        resize(global_settings, local_settings, file)


def get_local_settings(settings):
        local_settings = {}
        local_settings['output_size_h'] = input('enter desired horizontal size in pixels: ')
        local_settings['filter'] = input('image resampling (type: hard or soft): ')
        local_settings['resampling'] = get_filter(filter) 
        local_settings['output_format'] = input('add output format (type: JPEG, PNG, or GIF): ')
        regex = r'.+[^/]'
        search = re.findall(regex, settings['output_directory'])
        formatted_directory = search[0] + '/'
        local_settings['output_directory'] = formatted_directory 
        local_settings['output_extension'] = get_extension(local_settings['output_format'])
        local_settings['file_number'] = 0
        return local_settings
    
def resize(global_settings, local_settings, file):
    imagepath = global_settings['path']+file
    image = Image.open(imagepath)
    width, height = image.size
    output_scale_y = float(local_settings['output_size_h'])/width
    if(local_settings['output_format'] == 'PNG'):
        formatted_image = image.convert('RGBA')
    else:
        formatted_image = image.convert('RGB')
    output_image = formatted_image.resize(
        (int(local_settings['output_size_h']), int(output_scale_y*height)), resampling)
    if global_settings['multiple_files']==False:
        output_image.save(local_settings['output_directory'] + global_settings['basename'] + '.' + local_settings['output_extension'], local_settings['output_format'])
    if global_settings['multiple_files']==True: 
        # output_path = local_settings['output_directory'] + global_settings['basename'] + '.' + local_settings['file_number'] + '.' +  local_settings['output_extension'], local_settings['output_format']
        # print(output_path)
        output_image.save(local_settings['output_directory'] + global_settings['basename'] + '.' + local_settings['file_number'] + '.' +  local_settings['output_extension'], local_settings['output_format']) 
    
       