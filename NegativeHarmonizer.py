import argparse
import midi


def get_mirror_axis(tonic):
    return tonic + 3.5


def mirror_note_over_axis(note, axis):
    original_note_distance = axis - note
    return int(axis + original_note_distance)


def invert_tonality(pattern, tonic, ignored_channels):
    # print('tonic ' + str(tonic))
    mirror_axis = get_mirror_axis(tonic)
    # print('axis ' + str(mirror_axis))
    for track in pattern:
        for note in track:
            if type(note) is midi.NoteOnEvent or type(note) is midi.NoteOffEvent:
                if note.channel not in ignored_channels:
                    # print('original note ' + str(note.data[0]))
                    mirrored_note = mirror_note_over_axis(note.data[0], mirror_axis)
                    # print('mirrored_note ' + str(mirrored_note))
                    note.data[0] = mirrored_note


def main(input_file, tonic=midi.C_5, ignored_channels=[]):
    extension = ".mid"
    pattern = midi.read_midifile(input_file + extension)

    invert_tonality(pattern, tonic, ignored_channels)
    midi.write_midifile(input_file + "_negative" + extension, pattern)


parser = argparse.ArgumentParser(description='Negative Harmonize a midi file.')

parser.add_argument('file', metavar='f',
                    help='the input midi file (with no extension .mid)')
parser.add_argument('--tonic', type=int, default=55,
                    help='the tonic')
parser.add_argument('--ignore', type=list, nargs="+", default=[],
                    help='the midi channels to ignore (usually 9)')

args = parser.parse_args()

main(input_file=args.file, tonic=args.tonic, ignored_channels=args.ignore)
