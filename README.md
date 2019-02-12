# NegativeHarmonizer
NegativeHarmonizer is a simple python program to invert the tonality of a music file. This works very well for compositions like Bach's fugues. If you try it on popular music, you'll probably need to transpose the instruments back into their proper ranges, as the bass will be on the top. Beyond the fun of negative-harmonizing songs you know, this is a useful tool for composers and producers to add variations to their work.

Dependencies:
* Python 3
* mido 
    * `pip install mido`

Usage:

`python NegativeHarmonizer.py midifile.mid --tonic 55 --ignore 9`

This examples creates a new midifile named midifile_negative.mid that's been flipped over middle C and doesn't alter channel 9 because we don't want to alter the drums.


You can hear more examples of what can be done with NegativeHarmonizer on my YouTube channel (with some neat Tonnetz Lattice visualizations): https://www.youtube.com/watch?v=NDDE3Omt-DY

Some background on Negative Harmony from Jacob Collier: https://youtu.be/DnBr070vcNE?t=1m31s
