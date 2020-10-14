def loadAsLoL(file, compression="none"):
    if compression == 'none':
        with open(file, 'r') as inFile:
            LoS = inFile.read().splitlines()
            LoL = []
            for record in LoS:
                LoL.append(record.split(' '))
        return LoL
    elif compression == 'zip':
        import zipfile as z
        import os
        compressedFile = os.path.basename(os.path.splitext(file)[0])
        with z.ZipFile(file, 'r') as inFile:
            LoS = inFile.read(compressedFile).splitlines()
            LoL = []
            for record in LoS:
                LoL.append(record.decode().split())
        return LoL

