import os
import uuid


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(), ext)
    return os.path.join('upload/files', filename)
