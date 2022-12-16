#!/usr/bin/env python3

from . import renamer
from . import downloader
from configargparse import ArgumentParser


DEFAULT_CONFIG_FILES = ['./.gutdl.rc', '~/.gutdl.rc']


def main_arguments_parser():
    def str2bool(v):
        return str(v).lower() in ('yes', 'true', 't', 'y', '1')

    parser = ArgumentParser(description='gutdl: Gutenberg Downloader',
                            default_config_files=DEFAULT_CONFIG_FILES)
    parser.add('-c', '--config', is_config_file=True, help='config file path')

    parser.add_argument('--rename', '-r', type=str2bool, nargs='?',
                        default=False, help='Rename files.')
    parser.add_argument('--output_path', '-o', type=str, nargs='?',
                        help='Book folder.')
    parser.add('catalog_numbers', nargs='+', help='Catalog Numbers to Download.')

    return parser


def main():
    args = main_arguments_parser().parse_args()
    folder_path = args.output_path or "."

    if args.rename:
        renamer.rename_files_in_folder(folder_path)
    else:
        for book_number in args.catalog_numbers:
            downloader.download_book(folder_path, book_number)


if __name__ == "__main__":
    main()