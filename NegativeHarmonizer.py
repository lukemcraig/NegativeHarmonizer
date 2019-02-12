from __future__ import division
import argparse
import os

import mido


def get_mirror_axis(tonic):
    return tonic + 3.5


def mirror_note_over_axis(note, axis):
    original_note_distance = axis - note
    return int(axis + original_note_distance)


def invert_tonality(pattern, tonic, ignored_channels):
    # print('tonic ' + str(tonic))
    mirror_axis = get_mirror_axis(tonic)
    # print('axis ' + str(mirror_axis))
    original_octaves = {}
    for i, track in enumerate(pattern.tracks):
        track_avg_notes = []
        for note in track:
            if type(note) is mido.NoteOnEvent:
                track_avg_notes.append(note.data[0])
        if len(track_avg_notes) > 0:
            track_avg_note = sum(track_avg_notes) / len(track_avg_notes)
            original_octaves[i] = track_avg_note
            try:
                track_text = track[0].text
            except AttributeError:
                track_text = i
            print(track_text, track_avg_note)

    for track in pattern:
        for note in track:
            if type(note) is mido.NoteOnEvent or type(note) is mido.NoteOffEvent:
                if note.channel not in ignored_channels:
                    # print('original note ' + str(note.data[0]))
                    mirrored_note = mirror_note_over_axis(note.data[0], mirror_axis)
                    # print('mirrored_note ' + str(mirrored_note))
                    note.data[0] = mirrored_note
    print("---")
    new_octaves = {}
    for i, track in enumerate(pattern):
        track_avg_notes = []
        for note in track:
            if type(note) is mido.NoteOnEvent:
                track_avg_notes.append(note.data[0])
        if len(track_avg_notes) > 0:
            track_avg_note = sum(track_avg_notes) / len(track_avg_notes)
            new_octaves[i] = track_avg_note
            try:
                track_text = track[0].text
            except AttributeError:
                track_text = i
            print(track_text, track_avg_note)

    for i, track in enumerate(pattern):
        if original_octaves.has_key(i):
            notes_distance = original_octaves[i] - new_octaves[i]
            octaves_to_transpose = round(notes_distance / 12)
            for note in track:
                if type(note) is mido.NoteOnEvent or type(note) is mido.NoteOffEvent:
                    if note.channel not in ignored_channels:
                        transposed_note = note.data[0] + (octaves_to_transpose * 12)
                        note.data[0] = int(transposed_note)

    print("---")
    for i, track in enumerate(pattern):
        track_avg_notes = []
        for note in track:
            if type(note) is mido.NoteOnEvent:
                track_avg_notes.append(note.data[0])
        if len(track_avg_notes) > 0:
            track_avg_note = sum(track_avg_notes) / len(track_avg_notes)
            try:
                track_text = track[0].text
            except AttributeError:
                track_text = i
            print(track_text, track_avg_note)


def main(input_file, tonic=72, ignored_channels=[]):
    # 72=C5
    root, ext = os.path.splitext(input_file)
    pattern = mido.MidiFile(input_file)

    invert_tonality(pattern, tonic, ignored_channels)
    mido.write_midifile(root + "_negative" + ext, pattern)


parser = argparse.ArgumentParser(description='Negative Harmonize a midi file.')

parser.add_argument('file', metavar='f',
                    help='the input midi file (with no extension .mid)')
parser.add_argument('--tonic', type=int, default=55,
                    help='the tonic')
parser.add_argument('--ignore', type=list, nargs="+", default=[],
                    help='the midi channels to ignore (usually 9 for drums)')

args = parser.parse_args()

main(input_file=args.file, tonic=args.tonic, ignored_channels=args.ignore)
