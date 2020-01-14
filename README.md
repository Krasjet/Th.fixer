# Th.fixer

[Th.fixer](https://github.com/Krasjet/Th.fixer) is a simple Python script that removes the `Th`, `TT` ligatures (and its friends), which can be found in [Linux Libertine](https://sourceforge.net/projects/linuxlibertine/), [Alegreya](https://www.huertatipografica.com/en/fonts/alegreya-ht-pro), [Cormorant](https://github.com/CatharsisFonts/Cormorant), and many [Adobe Originals](https://www.adobe.com/products/type/adobe-type-originals.html) fonts, from a font's standard ligature set (`'liga'`).

![Th ligatures](./imgs/th_ligature.png)

## What's wrong with the `Th` ligature?

This is really an opinionated patcher.

I'm not against the `Th` ligature (and the similar `TT` ligature in Cormorant and Adobe Arno Pro). When used correctly, the ligature can look absolutely gorgeous (see the demo of [Hoefler Text](https://www.typography.com/fonts/hoefler-text/overview) and [Expo Serif Pro](https://typeculture.com/foundry/font-collection/expo-serif-pro/) for the correct way to use it). The problem is—in most instances, it should not be turned on **by default**, i.e. as part of the standard ligatures (`'liga'`). I consider this a design flaw, so I would call this script a "fixer" rather than a "patcher".

I agree that the spacing between `T` and `h` in some fonts (e.g. Adobe Garamond Pro) appears to be too large if you stare at this combination for long enough, and creating a ligature for them is certainly an easy way to fix this problem.

However, the `th` bigram is way too common in English. For example, you can find it in `the`, `this`, `that`, `those`, `these`, `thus`, `they`, etc., and, unfortunately, these words frequently occur as the first word of a sentence or even a paragraph so they are often capitalized. A ligature can be significantly more noticeable than a slightly larger gap between the two letters. Because I see this combination so often, my eyes can sometimes ignore the apparent gap between `Th` but the ligature, in contrast, is pulling too much attention from me. The `Th` ligature can be very disturbing if you use it in body text.

Being part of the standard ligatures (`'liga'`) means you can't turn this off unless you also turn off more reasonable ligatures like `fi`, `fj`, `fl`, etc. The `Th` ligature should be part of the discretionary ligatures `'dlig'`, along with ligatures for `ct`, `st`, etc., instead of the standard ligatures (`'liga'`) in most cases. However, this patch only removes the ligature from `'liga'` without putting it back to `'dlig'` since it is much easier to bring up the glyph for the ligature than removing it globally.

Note that I said the `Th` ligature should not be part of the standard ligatures **in most cases**. This is because there are instances when the `Th` ligature can be a legit choice—swash letters and calligraphic fonts.

![swash letters](./imgs/th_swash.png)

[Calligraphy](https://www.printmag.com/featured/flawed-typefaces/) is where this ligature came from. If the swash `T` is not connected to `h` in some way, there would be a big gap between them. It is something less tolerable in a calligraphic font because most letter pairs are connected in some way. I would consider the `Th` ligature necessary here and, to be honest, they look pretty good in this context. Therefore, the script will keep the ligatures for swash letters by default. On the other hand, for non-calligraphic fonts and non-swash letters, the ligature can look very strange.

## Why patch the font?

In fact, you don't have to. This is the last resort.

If you are using professional typesetting software, there are usually workarounds, though they might not be elegant. For example, you can use the [GREP](https://helpx.adobe.com/indesign/using/find-change.html#search_using_grep_expressions) feature to apply styles selectively in InDesign. There are also some ugly [workarounds](https://tex.stackexchange.com/questions/211202/suppress-specific-ligature-in-xelatex) in XeTeX and LuaTeX.

However, not every typesetting software supports a full set of OpenType features and scripting capabilities that allows you to turn on/off a single ligature rule (in fact, most of them don't). This is why I wrote this script.

Unfortunately, many foundries forbid modifications to the font file you purchased (which I think is absurd. Please support [indie foundries](https://www.harbortype.com/about/eula/) with less restrictive licensing terms), so you have to be cautious before you use patched fonts. I also do not recommend distributing patched fonts, either.

## Usage

To use this script, you first need to install [FontForge](https://fontforge.org) and register it as a [Python extension](https://fontforge.org/en-US/documentation/scripting/python/#fontforge-as-a-python-extension).

If you are using Arch Linux, simply install the package [fontforge](https://www.archlinux.org/packages/extra/x86_64/fontforge/) by

```bash
$ pacman -S fontforge
```

Unfortunately, FontForge is not available on [PyPI](https://pypi.org/), so you have to install it manually.

The script takes a single argument by default—the filename of the font file to be modified. If you want all the default behaviors, you can run the script by

```bash
$ ./thfixer.py font.otf
```

The output file will be in `out/font.otf`.

There are some optional arguments for further customizations. You can see all the options by

```bash
$ ./thfixer.py -h
```
which will output

```
usage: thfixer.py [-h] [-s] [-t] [-d OUTPUT_DIR] [-o OUT_FILENAME] [-f]
                  filename

Remove the 'Th' ligature (and its friends) from a font's standard ligature set
('liga').

positional arguments:
  filename              name of the input file

optional arguments:
  -h, --help            show this help message and exit
  -s, --fix-swash       include this flag if you want to remove the 'Th'
                        ligature for swash 'T' as well
  -t, --fix-tt          include this flag if you want to remove the 'TT'
                        ligature as well
  -d OUTPUT_DIR, --output-dir OUTPUT_DIR
                        the modified font will be saved to this directory
                        (default 'out')
  -o OUT_FILENAME, --out-filename OUT_FILENAME
                        name of the output file. the input filename will be
                        used if this option is not supplied
  -f, --use-fontname    include this flag if you want the output filename to
                        be the builtin fontname. if this flag is enabled, out-
                        filename will be ignored
```

For example, if you want to enable `fix-swash`, `fix-tt`, `use-fontname` options and set the output directory to `fixed`, then you can run the script by

```bash
$ ./thfixer.py -stf -d fixed font.otf
```

## Further reading

For some similar opinions, see

- [The Elements of Typographic Style](https://www.amazon.com/dp/0881792128/) by Robert Bringhurst
- [Flawed Typefaces](https://www.printmag.com/featured/flawed-typefaces/) by Paul Shaw
- [Butterick’s Practical Typography - Ligatures](https://practicaltypography.com/ligatures.html) by Matthew Butterick

## Image credits

The font used in the first image is [Garibaldi](https://www.harbortype.com/fonts/garibaldi/) by Henrique Beier. It is one of my favorites. The `Th` ligature in the font is discretionary so no patching is required.

The font used in the second image is [Garamond Premier Pro](https://www.harbortype.com/fonts/garibaldi/) by Robert Slimbach.

## License

The script is licensed under CC-BY-NC 4.0, but for the images in this README, all rights are reserved. (c) 2020 Krasjet
