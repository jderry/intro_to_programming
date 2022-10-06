''' python 2!
    credit: https://stackoverflow.com/questions/22646623/how-to-read-text-files-in-a-zipped-folder-in-python
'''

import os
import zipfile

with zipfile.ZipFile('archive.zip') as z:
    for filename in z.namelist():
        if not os.path.isdir(filename):
            # read the file
            with z.open(filename) as f:
                for line in f:
                    print line

