def dms2dd(dms):
    '''(str) -> float
       Given a string with dd°mm'ss" format, return the decimal degree equivalent.
       Input must include minutes and seconds.
       Note that because ' and " are used to designate minutes and seconds,
       the string must be passed in as a docstring.
       Allows for latitude and longitude readings.
       >>>dms2dd("""51°36'9.18"N""")
       51.60255
       >>>dms2dd("""78°55'44.33324"""")
       78.92898145555556
       >>>dms2dd("""-180°0'0" """) # here, because of double-quotes, we need a trailing space
       # this is because otherwise the parser groups the seconds double-quote with the docstring double-quotes
       # this can be avoided by using a docstring of single-quotes
       -180.0
       credit: this function developed from inti's answer in:
       https://stackoverflow.com/questions/33997361/how-to-convert-degree-minute-second-to-degree-decimal
    '''
    import re
    deg, minutes, seconds, direction =  re.split('[°\'"]', dms)
    return (float(deg) + float(minutes)/60 + float(seconds)/(3600)) \
           * (-1 if direction in 'WwSs' and direction != '' else 1)

