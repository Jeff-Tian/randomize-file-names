import os
import string
import random

for subdir, dirs, files in os.walk('./'):
    for file in files:
        new_file_name = ''.join([random.choice(string.ascii_uppercase) for _ in range(8)])
        lower = file.lower()
        if lower.endswith('.jpg') or lower.endswith('.png') or lower.endswith('.jpeg') or lower.endswith('gif'):
            ext = os.path.splitext(file)[1]
            print(file, '-->', new_file_name + ext)
            os.rename(file, new_file_name + ext)
