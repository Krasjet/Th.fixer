Th.fixer
========

Th.fixer is a simple Python script that removes the `Th`, `TT` ligatures (and
their friends), which can be found in [Linux Libertine][libertine],
[Alegreya][alegreya], [Cormorant][cormorant], and many [Adobe Originals][adobe]
fonts, from a font's standard ligature set (`'liga'`).

![Th ligatures](./imgs/th_ligature.png)

For more information, see [here][thfixer].

[libertine]: https://sourceforge.net/projects/linuxlibertine/
[alegreya]: https://www.huertatipografica.com/en/fonts/alegreya-ht-pro
[cormorant]: https://github.com/CatharsisFonts/Cormorant
[adobe]: https://www.adobe.com/products/type/adobe-type-originals.html

[thfixer]: https://krasjet.com/voice/Th.fixer/

Usage
-----

To use this script, you first need to install [FontForge][fontforge] and
register it as a [Python extension][python_ext].

[fontforge]: https://fontforge.org
[python_ext]: https://fontforge.org/en-US/documentation/scripting/python/#fontforge-as-a-python-extension

If you are using Arch Linux, simply install the package [fontforge][arch] by

[arch]: https://www.archlinux.org/packages/extra/x86_64/fontforge/

```bash
$ pacman -S fontforge
```

Unfortunately, FontForge is not available on [PyPI][pypi], so you
have to install it manually.

[pypi]: https://pypi.org/

The script takes a single argument by default—the filename of the font file to
be modified. If you want all the default behaviors, you can run the script by

```bash
$ ./thfixer.py font.otf
```

The output file will be in `out/font.otf`.

There are some optional arguments for further customizations. You can see all
the options by

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

For example, if you want to enable `fix-swash`, `fix-tt`, `use-fontname`
options and set the output directory to `fixed`, then you can run the script by

```bash
$ ./thfixer.py -stf -d fixed font.otf
```
