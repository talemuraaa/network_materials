import os

def get_image_path(subfolder,filename):
    this_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(this_dir, "..", "images",subfolder, filename)

