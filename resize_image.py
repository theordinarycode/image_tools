#comment tester

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

def scale_images():
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
    first_pass = True
    output_size_h = input('enter desired horizontal size in pixels: ')
    filter = input('image resampling (type: hard or soft): ')
    resampling = get_filter(filter) 
    output_format = input('add output format (type: JPEG, PNG, or GIF): ')
    output_directory = input('output directory: ')
    
    with alive_bar(len(files_list)) as bar:
        for image_name_extension in files_list:
            image_name = image_name_extension.rsplit('.', 1)[0]
            image_path = files_path + image_name_extension
            image = Image.open(image_path)
            width, height = image.size
            if first_pass == True:
                output_scale_y = float(output_size_h)/width
                output_extension = get_extension(output_format)
                regex = r'.+[^/]'
                search = re.findall(regex, output_directory)
                formatted_directory = search[0] + '/'
                first_pass = False

            if(output_format == 'PNG'):
                formatted_image = image.convert('RGBA')
            else:
                formatted_image = image.convert('RGB')

            output_image = formatted_image.resize(
                (int(output_size_h), int(output_scale_y*height)), resampling)
            output_image.save(
                formatted_directory + image_name + '.'
                + output_extension, output_format) 
            bar()

scale_images()
    

