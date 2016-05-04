try:
    import ConfigParser as Config
except ImportError:
    import configparser as Config


def ConfigSectionMap(file):
    """Parse the ini into a dictionary."""
    config = Config.ConfigParser()
    config.read(file)
    section = config.sections()[0]

    dict1 = {}
    options = Config.options(section)
    import pdb; pdb.set_trace()
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

