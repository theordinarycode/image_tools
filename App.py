from process_images import process_images
from resize_image import resize_images, get_local_settings
from get_settings import get_settings

settings = get_settings()
resize_images(settings)
