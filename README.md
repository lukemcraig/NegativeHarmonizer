# NegativeHarmonizer
NegativeHarmonizer is a simple python program to invert the tonality of a music file. This works very well for compositions like Bach's fugues. If you try it on popular music, you'll probably need to transpose the instruments back into their proper ranges, as the bass will be on the top. Beyond the fun of negative-harmonizing songs you know, this is a useful tool for composers and producers to add variations to their work.

Dependencies:
* Python 3
* mido 
    * `pip install mido`

Usage:

`python NegativeHarmonizer.py midifile.mid --tonic 60 --ignore 9 --adjust-octaves`

This example command 
1. creates a new midifile named midifile_negative.mid 
2. flipped over middle C (midi note number 60)
3. channel 9 is unaltered because we don't want to change the drums.
4. the tracks are transposed to be close to their original octave, so the bass guitar will stay in the bass range etc.


You can hear more examples of what can be done with NegativeHarmonizer on my YouTube channel (with some neat Tonnetz Lattice visualizations): <a href="http://www.youtube.com/watch?feature=player_embedded&v=NDDE3Omt-DY" target="_blank"><img src="http://i3.ytimg.com/vi/NDDE3Omt-DY/hqdefault.jpg" alt="Beethoven, Symphony 5, 1st movement: Negative Harmony" width="240" height="180" border="10" /></a>
 
Some background on Negative Harmony from Jacob Collier: https://youtu.be/DnBr070vcNE?t=1m31s
