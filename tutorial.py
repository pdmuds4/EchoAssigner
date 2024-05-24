from echo_assigner import EchoAssigner

INPUT_MIDI = "" # input midi file path
OUTPUT_MIDI = "output.mid" # output midi file path

ea = EchoAssigner(INPUT_MIDI, distmethod=0) # create EchoAssigner instance

ea.cui.show_params() # check settings params

ea.cui.show_assigned_part() # show assigned measure

ea.cui.accuracy() # show accuracy of simulaly of input melody and knowledge base melody

stream = ea.create.fit_stream() # create m21.stream.Stream

stream.write("midi", OUTPUT_MIDI) # write midi file