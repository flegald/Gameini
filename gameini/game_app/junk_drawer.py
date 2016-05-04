try:
    import ConfigParser as configparser
except ImportError:
    import configparser

import logging

logger = logging.getLogger(__name__)


def config_section_map(file):
    """Parse the ini into a dictionary."""
    if file.tell():
        file.seek(0)
    config = configparser.ConfigParser()
    bytes_content = file.read()
    str_content = bytes_content.decode('utf8')
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
    return dict1

