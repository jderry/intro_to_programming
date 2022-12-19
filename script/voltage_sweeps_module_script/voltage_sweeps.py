import voltage_sweeps_module as vs

constDict = vs.initialize()
# here, you add key/value pairs of math expressions from constants in dict
constDict['expr0'] = 1/\
                    (float(constDict['CSiO2(F/cm2)']) * float(constDict['W/L']))

runDict = vs.put_datafile_contents_into_runDict(constDict)
vs.process_items_in_runDict(runDict, constDict)
