from PIL import Image, PngImagePlugin

def get_data():
    data = {}
    data['path_to_image'] = input('path to your image: ')

    attributes = input('add required attributes as comma separated list: ')
    print(attributes.split(','))
    for attribute in [x.strip() for x in attributes.split(',')]:
        if len(attribute) > 0:
            data[attribute] = input('add attribuet "{}" value: '.format(attribute))
    print(data)

    return data

def display_image(data):
    image = Image.open(data['path_to_image'])
    image.show()

def add_metadata(data):
    print(data['path_to_image'])
    info = PngImagePlugin.PngInfo()
    for index, attribute in enumerate(data):
        if index>0: 
            print(attribute, data[attribute])
            info.add_text(attribute, data[attribute])
    image = Image.open(data['path_to_image']) 
    image.save(data['path_to_image'], pnginfo=info)

def read_metadata(data):
    #property_array = [x.strip() for x in properties.split(',')]
    print('read metadata')
    image = Image.open(data['path_to_image'])
    #print(image.text, type(image.text))
    attributes = image.text
    for key in attributes:
        print(key, [x.strip() for x in attributes[key].split(',')])


if __name__ == "__main__":
    data = get_data()
    #display_image(data)
    add_metadata(data)
    read_metadata(data)




# pathToImage = input('path to your image: ')

# info = PngImagePlugin.PngInfo()
# imageTitle = 'myImageFromCombinator'
# text = input('text to add to image metadata: ')
# elementsarray = ['blood', 'guts', 'slime']
# elementsstring = ','.join(elementsarray)
# info.add_text("text", text)
# info.add_text("title", imageTitle)
# info.add_text("ZIP", "VALUE", zip=True)
# info.add_text('elements', elementsstring)

# im = Image.open(pathToImage) 

# outPutPath = input('path to output: ')
# im.save(outPutPath+'/'+imageTitle+'.png', "PNG", pnginfo=info)

# im2 = Image.open(outPutPath+'/'+imageTitle+'.png')
# # print(im2.text["text"])
# # print(im2.text["title"])
# print(im2.text)
# print(im2.text['elements'].split(','))