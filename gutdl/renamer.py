import os
import re
from fnmatch import fnmatch

from .downloader import get_title_from_number


def get_number_from_filename(file_name):
    # pg24737-images.mobi
    # pg4018.epub
    regex_file_name = "pg[0-9]+(-|\.)"
    match = re.match(regex_file_name, file_name)
    return match.group()[2:-1] if match else None


def rename_files_in_folder(folder_path):
    os.chdir(folder_path)
    file_names = os.listdir('.')
    for file_name in file_names:
        book_number = get_number_from_filename(file_name)
        exists = os.path.exists(file_name)
        if book_number and exists:  # exists
            without_extention = file_name.rsplit(".", 1)[0]
            pattern = without_extention + '.*'
            old_names = [fn for fn in os.listdir('.') if fnmatch(fn, pattern)]
            title = get_title_from_number(book_number)
            for old_name in old_names:
                extension = old_name.rsplit(".", 1)[1]
                new_name = title + "." + extension
                os.rename(old_name, new_name)
