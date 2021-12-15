from process_images import process_images
from resize_image import resize_images, get_local_settings
from get_settings import get_settings
from rename_files import rename_files
from add_metadata import add_metadata
from add_metadata import read_metadata

# settings = get_settings()
# if 'rename' in settings['commands']:
#     print('rename is true')
#     rename_files(settings)
# if 'resize' in settings['commands']:
#     print('resize is true')
#     resize_images(settings)
# if 'add_metadata' in settings['commands']:
#     print('add metadata is true')
#     add_metadata(settings)
# if 'combine_images' in settings['commands']:
#     print('combine images is true')

metadata = read_metadata('/Users/wolf/Downloads/zombies/WickedWilly.0000.png')
print(metadata)

