from process_images import process_images
from resize_image import resize_images, get_local_settings
from get_settings import get_settings
from rename_files import rename_files


settings = get_settings()
print(settings)
if 'rename' in settings['commands']:
    print('rename is true')
    rename_files(settings)
if 'resize' in settings['commands']:
    print('resize is true')
    resize_images(settings)
if 'addMetaData' in settings['commands']:
    print('add metadata is true')
if 'combineImages' in settings['commands']:
    print('combine images is true')

