import os

def get_absolute_location_from_script(script_path, path):
    dir_name = os.path.dirname(os.path.realpath(script_path))
    return os.path.join(dir_name, path)
