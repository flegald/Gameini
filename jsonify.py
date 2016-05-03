"""Convert files to json."""


def to_json(file):
    """Convert ini to JSON like thing."""
    ini = open(file, 'r')
    ini = ini.readlines()
    settings_file = open('settings.json', 'w')
    settings_file.write("{")
    # import pdb; pdb.set_trace()
    for line in ini:
        if '[' == line[0]:
            settings_file.write('"' + line[1:-2] + '"' + ': {')
        else:
            line = line.split('=')
            settings_file.write('"{0}": "{1}", '.format(line[0], line[1][0]))
    settings_file.write("}")


to_json('practice.ini')
