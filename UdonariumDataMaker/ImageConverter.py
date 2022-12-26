import os
import hashlib
import shutil 

def convert(input_path, output_root) :
    new_image_name = _get_new_image_name(input_path)
    path, ext = os.path.splitext(input_path)
    out = output_root + "\\" + new_image_name + ext
    shutil.copyfile(input_path,out)
    return new_image_name

def _get_new_image_name (img_path):
    with open(img_path, 'rb') as file:
        fileData = file.read()
        # sha256
        hash_sha256 = hashlib.sha256(fileData).hexdigest()
        return hash_sha256[0:64]