def extract_zip(input_zip):
    '''(str)-> dict
    Given a zipped file's path as input string, return a dictionary of the zipped file's contents.
    '''
    from zipfile import ZipFile
    input_zip = ZipFile(input_zip)
    return {name: input_zip.read(name) for name in input_zip.namelist()}
