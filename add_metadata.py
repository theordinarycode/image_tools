from PIL import Image, PngImagePlugin
import os
import re

def add_metadata(settings):
    print(settings)
    data_template = set_data()
    for file in sorted(os.listdir(settings['path'])):
        if not file.startswith('.'):
            print('Let\'s add metadata to this file:', file)
            image = Image.open(settings['path']+file)
            image.show()
            data = add_data(data_template)
            info = PngImagePlugin.PngInfo()

            for attribute in data:
                info.add_text(attribute, data[attribute])
            
            image.save(settings['path']+file, pnginfo=info)
            read_metadata(settings['path']+file)
            
def set_data():
    print('Let\'s add meta-data to our image/s...')
    return input('We can add custom metadata attributes. Please type your required metadata attributes as a comma separated list (ex: myCustomMetadataOne,myCustomMetadataTwo,etc): ')
    
def add_data(data_template):
    data = {}
    for attribute in [x.strip() for x in data_template.split(',')]:
        if len(attribute) > 0:
            data[attribute] = input('add attribute "{}" value: '.format(attribute))
    return data

def read_metadata(file):
    image = Image.open(file)
    attributes = image.text
    print('metadata:')
    # for key in attributes:
    #     attributeArray = [x.strip() for x in attributes[key].split(',')]
    #     if len(attributeArray)>1:
    #         print(key+":", attributeArray)
    #     else:
    #         print(key+":", attributeArray[0])
    return attributes



