
'''
Place to store useful variables that will be used across the project. This
will mainly be used for paths.

Author: Evie Mills
Date: May 2024
'''

import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


project = os.environ.get('PROJECT_ROOT',None)

assert project is not None, '.env not loaded correctly, change path in load_dotenv()'

project = Path(project)
code = project / 'code'
data = project / 'data'

paths = {'project': project,
        'code': code,
        'data' : data,
        'raw':  data / 'raw',
        'processed': data / 'processed',
        'dataset': data / 'dataset',
        'models' : project / 'models'
        }
