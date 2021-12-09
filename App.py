from process_images import process_images
from resize_image import resize_images, get_local_settings
from get_settings import get_settings
from rename_files import rename_files

settings = get_settings()
print(settings)
rename_files(settings)
resize_images(settings)
