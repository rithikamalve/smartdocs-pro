import os

def get_file_info(file):
    filename = file.name
    ext = os.path.splitext(filename)[1].lower()
    return filename, ext 