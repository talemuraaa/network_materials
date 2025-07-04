import os

def get_html_path(subfolder,filename):
    this_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(this_dir, "..", "html_files",subfolder, filename)