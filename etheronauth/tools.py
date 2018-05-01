import os
import json

from etheronauth import globalvars
from etheronauth import log

def get_json(filename):
    try:
        data = json.load(open(get_dir() + "resources/" +filename))
        return data
    except IOError as e:
        log.out.error('File {} could not be read'.format(filename))
        print (e)
        return False


def write_json(filename, data):
    try:
        with open(get_dir() + "resources/" +filename, 'w') as outfile:
            json.dump(data, outfile)
            log.out.debug('File {} written'.format(filename))
            return True
    except IOError as e:
            log.out.error('File {} could not be written'.format(filename))
            print (e)
            return False

def get_file(filename):
    try:
        file = open(get_dir() + "resources/" +filename, "r")
        data = file.read()
        return data
    except IOError as e:
        log.out.error('File {} could not be read'.format(filename))
        print (e)
        return False

def write_file(filename, data):
    try:
        file = open(get_dir() + "resources/" +filename,"w")
        file.write(data)
        log.out.debug('File {} written'.format(filename))
        return True
    except IOError as e:
        log.out.error('File {} could not be written'.format(filename))
        print (e)
        return False

def get_dir():
    return globalvars.__path__
