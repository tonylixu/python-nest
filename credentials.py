from __future__ import print_function
from __future__ import absolute_import
'''This python file retrieves the secret that you stored in
a local configruation file. This way you don't need to expose
the important information such as password or api keys in the
program
This script reads ~/._config file and finds matching values
Example:
$ cat ~/.nest_config
nest:
    client_id: '874432hkjh'
    client_secret: '8da7f8s7fdfsfdsfs'
Then, if you call the from_secret function:
    from_secret('nest', 'client_id') returns '874432hkjh'
    from_secret('nest', 'client_secret') returns '8da7f8s7fdfsfdsfs'
'''
from os.path import expanduser
import yaml

user_home_dir = ''
try:
    user_home_dir = expanduser('~')
    with open('{0}/.nest_config'.format(user_home_dir), 'r') as input:
        # Parse yml file into dict
        nest_data = yaml.load(input)
except:
    print('Could not find {0}/.nest_config file. Please create one'.format(user_home_dir))

def get_credentials(category, field, override=None):
    if not override is None:
        val = override
    else:
        if category in nest_data:
            val = nest_data[category][field]
        else:
            val = None
    if val is None:
        raise Exception('No {0} {1} specifed in .nest_config'.format(category, field))
    return val
