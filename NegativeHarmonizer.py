import argparse
import os

import mido


def get_mirror_axis(tonic):
    return tonic + 3.5


def mirror_note_over_axis(note, axis):
    original_note_distance = axis - note
    return int(axis + original_note_distance)


def invert_tonality(mid, tonic, ignored_channels):
    # print('tonic ' + str(tonic))
    mirror_axis = get_mirror_axis(tonic)
    # print('axis ' + str(mirror_axis))
    original_octaves = {}
    for i, track in enumerate(mid.tracks):
        track_avg_notes = []
        for note in track:
            # if type(note) is mido.NoteOnEvent:
            if note.type == 'note_on':
                track_avg_notes.append(note.note)
        if len(track_avg_notes) > 0:
            track_avg_note = sum(track_avg_notes) / len(track_avg_notes)
            original_octaves[i] = track_avg_note
            try:
                track_name = track.name
            except AttributeError:
                track_name = i
            print(track_name, track_avg_note)

    for track in mid.tracks:
        for note in track:
            if note.type == 'note_on' or note.type == 'note_off':
                if note.channel not in ignored_channels:
                    # print('original note ' + str(note.data[0]))
                    mirrored_note = mirror_note_over_axis(note.note, mirror_axis)
                    # print('mirrored_note ' + str(mirrored_note))
                    note.note = mirrored_note
    print("---")

    new_octaves = {}
    for i, track in enumerate(mid.tracks):
        track_avg_notes = []
        for note in track:
            if note.type == 'note_on':
                track_avg_notes.append(note.note)
        if len(track_avg_notes) > 0:
            track_avg_note = sum(track_avg_notes) / len(track_avg_notes)
            new_octaves[i] = track_avg_note
            try:
                track_name = track.name
            except AttributeError:
                track_name = i
            print(track_name, track_avg_note)

    for i, track in enumerate(mid.tracks):
        if i in original_octaves:
            notes_distance = original_octaves[i] - new_octaves[i]
            octaves_to_transpose = round(notes_distance / 12)
            for note in track:
                if note.type == 'note_on' or note.type == 'note_off':
                    if note.channel not in ignored_channels:
                        transposed_note = note.note + (octaves_to_transpose * 12)
                        note.note = int(transposed_note)

    print("---")
    for i, track in enumerate(mid.tracks):
        track_avg_notes = []
        for note in track:
            if note.type == 'note_on':
                track_avg_notes.append(note.note)
                if len(track_avg_notes) > 0:
                    track_avg_note = sum(track_avg_notes) / len(track_avg_notes)
            try:
                track_name = track[0].text
            except AttributeError:
                track_name = i
            print(track_name, track_avg_note)


def main(input_file, tonic=55, ignored_channels=[]):
    root, ext = os.path.splitext(input_file)
    mid = mido.MidiFile(input_file)

    invert_tonality(mid, tonic, ignored_channels)
    mid.save(root + "_negative" + ext)


parser = argparse.ArgumentParser(description='Negative Harmonize a midi file.')

parser.add_argument('file', metavar='f',
                    help='the input midi file (with no extension .mid)')
parser.add_argument('--tonic', type=int, default=55,
                    help='the tonic')
parser.add_argument('--ignore', type=list, nargs="+", default=[],
                    help='the midi channels to ignore (usually 9 for drums)')

args = parser.parse_args()

main(input_file=args.file, tonic=args.tonic, ignored_channels=args.ignore)
