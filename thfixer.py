#!/usr/bin/env python3
"""
Th-fixer: remove the 'Th' ligature (and its friends) from a font's standard ligature set ('liga').

Author: Krasjet
Website: https://github.com/Krasjet/Th.fixer
Usage: see ./thfixer.py -h
"""
import fontforge
from argparse import ArgumentParser
from pathlib import Path

# You might want to change these to work with different fonts (e.g. Adobe Arno Pro has different names for swash letters)
T_VARIANTS = ['T', 'Tcaron', 'uni021A', 'uni0162', 'uni0164', 'Tcommaaccent', 'Tbar']
T_SWASH_VARIANTS = [t + '.swash' for t in T_VARIANTS]
H_VARIANTS = ['h']

parser = ArgumentParser(
    description="Remove the 'Th' ligature (and its friends) from a font's standard ligature set ('liga').")
parser.add_argument('filename', help="name of the input file")
parser.add_argument('-s', '--fix-swash', action='store_true',
                    help="include this flag if you want to remove the 'Th' ligature for swash 'T' as well")
parser.add_argument('-t', '--fix-tt', action='store_true',
                    help="include this flag if you want to remove the 'TT' ligature as well")
parser.add_argument('-d', '--output-dir', default='out',
                    help="the modified font will be saved to this directory (default 'out')")
parser.add_argument('-o', '--out-filename', default='',
                    help="name of the output file. the input filename will be used if this option is not supplied")
parser.add_argument('-f', '--use-fontname', action='store_true',
                    help="include this flag if you want the output filename to be the builtin fontname. if this flag is enabled, out-filename will be ignored")

args = parser.parse_args()

try:
    font = fontforge.open(args.filename)
except OSError as e:
    # file not found. error messages provided by fontforge
    exit(1)

for glyph in font.glyphs():
    if '_' not in glyph.glyphname:
        continue  # skip non-ligature glyphs
    for sub in glyph.getPosSub('*'):
        # only check standard ligatures
        if "'liga'" not in sub[0]:
            continue
        # matched Th ligature or swash Th ligature
        if (sub[2] in T_VARIANTS or (args.fix_swash and sub[2] in T_SWASH_VARIANTS))\
                and (sub[3] in H_VARIANTS or (args.fix_tt and sub[3] in T_VARIANTS)):
            # remove the subtable entry for this glyph
            glyph.removePosSub(sub[0])
            print("removed ligature for", glyph.glyphname)

ext = Path(args.filename).suffix

if args.use_fontname:
    out_filename = font.fontname + ext
else:
    if args.out_filename == '':
        out_filename = args.filename  # use input file name if output filename is empty
    else:
        out_filename = args.out_filename + ext

# make directory if not exist
Path(args.output_dir).mkdir(parents=True, exist_ok=True)

# generate the font
path = f"{args.output_dir}/{out_filename}"
try:
    font.generate(path)
    print("patched font has been saved to", path)
except OSError as e:
    exit(1)
