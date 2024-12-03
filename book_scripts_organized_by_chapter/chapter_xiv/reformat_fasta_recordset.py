def reformatFastaRecordSet(fastafile: str):
    ''' Given a fasta recordset in a text file,
        write out a text file of reformatted fasta records,
        one record per line.
    ''' 
    # read the fasta recordset into a list-of-strings
    with open(fastafile) as inFile:
        LoS = inFile.read().splitlines()
    with open('reformattedFastaFile', 'w') as outFile:
        # initialization
        head, data, record = '', '', ''
        for line in LoS:
            # the machine iterates
            # down the list of strings
            # one line at a time
            if line.startswith('>'):
                # if the line is 1st line of record,
                # first, write out the old record
                record = head[1:] + ' ' + data
                # ^^^ head[1:] is a slice
                # excluding the first character
                if record:
                    outFile.write(f"{record}\n")
                head, data = ' '.join(line.split()), ''
                # ^^^ re-initializa and re-instantiate
            else:
                # line is a data line
                # concatenate to data string
                # and update variable
                data = data + line

