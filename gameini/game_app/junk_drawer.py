"""File to store helper functions."""
import tempfile
try:
    import ConfigParser as configparser
except ImportError:
    import configparser

import logging

logger = logging.getLogger(__name__)


def config_section_map(file):
    """Parse the ini into a dictionary."""
    config = configparser.ConfigParser()
    str_content = reset_file(file)
    config.read_string(str_content)
    section = config.sections()[0]
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                logging.warn("skip: %s" % option)
        except:
            logging.error("exception on %s!" % option)
            dict1[option] = None
    return dict1, section


def reset_file(file):
    """Move file cursor back to byte 0 and set encoding."""
    file.seek(0)
    bytes_content = file.read()
    str_content = bytes_content.decode('utf8')
    return str_content


def change_settings(section, form_data, file):
    """Return file with new settings."""
    config = configparser.ConfigParser()
    str_content = reset_file(file)
    config.read_string(str_content)
    setting = section
    for item in form_data.keys():
        config.set(setting, item, form_data[item])


    temp = tempfile.TemporaryFile(suffix='ini', mode='w+')
    config.write(temp)
    temp.write(str_content)

    return temp

