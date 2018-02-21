import midi


def get_mirror_axis(tonic):
    return tonic + 3.5


def mirror_note_over_axis(note, axis):
    original_note_distance = axis - note
    return int(axis + original_note_distance)


def invert_tonality(pattern, tonic):
    # print('tonic ' + str(tonic))
    mirror_axis = get_mirror_axis(tonic)
    # print('axis ' + str(mirror_axis))
    for track in pattern:
        for note in track:
            if type(note) is midi.NoteOnEvent or type(note) is midi.NoteOffEvent:
                # print('original note ' + str(note.data[0]))
                mirrored_note = mirror_note_over_axis(note.data[0], mirror_axis)
                # print('mirrored_note ' + str(mirrored_note))
                note.data[0] = mirrored_note


def main(input_file, tonic=midi.C_5):
    extension = ".mid"
    pattern = midi.read_midifile(input_file + extension)

    invert_tonality(pattern, tonic)
    midi.write_midifile(input_file + "_negative" + extension, pattern)


main(input_file="midi_files/fugue-c-major", tonic=midi.C_5)
