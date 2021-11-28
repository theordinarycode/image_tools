from PIL import Image, PngImagePlugin
import os
import re


def get_path():
    print('Will you be processing multiple images?')
    test = input('type yes or no: ')
    multiple = False
    settings = []
    if test.lower() in ['yes', 'y'] :
        multiple = True
        settings.append(multiple)
        path = input('path to your images: ')
        settings.append(path+'/')
    else:
        settings.append(multiple) 
        path = input('full path to your image (including the image): ')
        settings.append(path)
    return settings
    
def add_data():
    data = {}
    attributes = input('add required attributes as comma separated list: ')
    for attribute in [x.strip() for x in attributes.split(',')]:
        if len(attribute) > 0:
            data[attribute] = input('add attribute "{}" value: '.format(attribute))
    return data

def display_image(settings, file):
    print(settings[1]+file)
    image = Image.open(settings[1]+file)
    image.show()

def add_metadata(data, settings, file):
    info = PngImagePlugin.PngInfo()
    for index, attribute in enumerate(data):
        if index>0: 
            info.add_text(attribute, data[attribute])
    image = Image.open(settings[1]+file)
    image.save(settings[1]+file, pnginfo=info)

def read_metadata(settings, file):
    image = Image.open(settings[1]+file)
    attributes = image.text
    for key in attributes:
        attributeArray = [x.strip() for x in attributes[key].split(',')]
        if len(attributeArray)>1:
            print(key+":", attributeArray)
        else:
            print(key+":", attributeArray[0])


def process_image(settings, file):
    display_image(settings, file)
    data = add_data()
    add_metadata(data, settings, file)
    read_metadata(settings, file)

if __name__ == "__main__":
    settings = get_path()
    print(settings)
    if settings[0] == True:
        files_list = [f for f in os.listdir(settings[1]) if not f.startswith('.')]
        files_list.sort()
        for file in files_list:
            print(settings[1]+file)
            process_image(settings, file)
    else:
        path = os.path.dirname(settings[1])
        print(path) 
        file = os.path.basename(settings[1])
        print(settings[1])
        process_image(settings, file)
    






