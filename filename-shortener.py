import os
import re
import argparse
import hashlib


def process_directory(directory, regex):
    filename_array = os.listdir(directory)

    for filename in filename_array:

        match = re.search('([^_]*)(.*(\\d{2})\\.(\\d{2})\\.(\\d{4}).*)(\\.\\w+)', filename)

        if match is not None:
            prefix = match.group(1)
            clutter = match.group(2)
            day = match.group(3)
            month = match.group(4)
            year = match.group(5)[2:]
            extension = match.group(6)
            hashed_clutter = hashlib.sha1(clutter).hexdigest()[:8]
            new_filename = year + month + day + '-' + prefix + '_' + hashed_clutter + extension

            print 'Renaming: [' + filename + '] => [' + new_filename + ']'
            os.rename(directory + '/' + filename, directory + '/' + new_filename)
        else:
            print 'Keeping [' + filename + ']'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    args = parser.parse_args()

    process_directory(args.directory, args.regex)


main()
