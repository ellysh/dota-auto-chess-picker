#!/usr/bin/env python3
import os
import ntpath
import sys
from csv import reader
from pkg_resources import resource_filename
from shutil import copyfile

if sys.platform == "win32":
    USER_PATH = os.path.expanduser("~") + "/AppData/Local/dac_picker/"
else:
    USER_PATH = os.path.expanduser("~") + "/.local/share/dac_picker/"

def get_filename(resource):
    return USER_PATH + ntpath.basename(resource)

def copy_resource_file(resource):
    path = get_filename(resource)

    if os.path.exists(path): return

    if not os.path.exists(USER_PATH):
        os.mkdir(USER_PATH)

    copyfile(resource, path)

class Csv(object):
    @staticmethod
    def load(file, max_column):
        result = {}
        with open(resource_filename("dac_picker", file)) as csv_file:
            csv_reader = reader(csv_file, delimiter=';')
            # Skip the columns headers
            next(csv_reader)

            for line in csv_reader:
                if max_column == 4:
                    result[line[0]] = [line[1], line[2], line[3], line[4]]
                elif max_column == 3:
                    result[line[1]] = [line[2], line[3], line[0]]
                else:
                    result[line[0]] = [line[1], line[2]]

        return result

    @staticmethod
    def load_combos(file):
        copy_resource_file(resource_filename("dac_picker", file))

        result = {}
        with open(get_filename(file)) as csv_file:
            csv_reader = reader(csv_file, delimiter=';')
            # Skip the columns headers
            next(csv_reader)

            for line in csv_reader:
                if not line[1] in result.keys():
                    result[line[1]] = []

                result[line[1]].append([line[0], line[2], line[3], line[4]])

        return result
