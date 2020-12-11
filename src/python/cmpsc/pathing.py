import os


def get(parent: str = None, *args: str):
    """
    :param parent: Name of the parent directory [Optional]
    :param args: The path to a file or directory.
    :return: Returns a complete path to a specified file or directory.
    """
    if parent is None:
        parent = ''
    nargs = [s.replace('/', os.pathsep).replace('\\', os.pathsep) for s in args if s.find('/') or s.find('\\')]
    return os.path.normpath(os.path.join(src_dir, parent, *nargs))


src_dir = os.path.dirname(__file__)
html_dir = get('../../html')
data_dir = get('../../data')
template_dir = get('../../../templates')
