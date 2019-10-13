# python-wrapper-cab-webservice

- [CAB-webservice](#cab-webservice)
- [How to use the class](#how-to-use-the-class)
  - [JSON](#json)
  - [DataFrame](#dataframe)
  - [CSV (Tabs)](#csv-tabs)
  - [Text (with Annotations)](#text-with-annotations)
  - [Raw Text](#raw-text)
  - [ltwxml](#ltwxml)
  - [List](#list)

Small Python wrapper class for the [CAB-webservice](https://kaskade.dwds.de/demo/cab/).

This class provides a simple interface to interact with B. Jurish’s [CAB-webservice](https://kaskade.dwds.de/demo/cab/) from within Python.

## CAB-webservice
The [CAB-webservice](https://kaskade.dwds.de/demo/cab/) was created by B. Jurish. For more information about the [CAB-webservice](https://kaskade.dwds.de/demo/cab/) please see:

> Jurish, B. Finite-state Canonicalization Techniques for Historical German. PhD thesis, Universität Potsdam, 2012 (defended 2011). URN [urn:nbn:de:kobv:517-opus-55789.](https://nbn-resolving.org/resolver?identifier=urn%3Anbn%3Ade%3Akobv%3A517-opus-55789)

## How to use the class

Download the `CabWebserviceWrapper.py` file. Put the file into the same folder where your other Python files or jupyter notebooks are located.

```Python
# Import the class
from CabWebserviceWrapper import CabWrapper
# Instantiate the class
CAB = CabWrapper()
# Set the return format: json, text, csv, raw, ltwxml, dataframe
CAB.format = 'json'
# Set the outputs you want (word, lemma, a/o pos), just concatenate them with pluses
CAB.output = 'word+lemma+pos'
# Query a text
CAB.getText('Jn jm war das Leben / vnd das Leben war das Liecht der Menschen / vnd das Liecht scheinet in der Finsternis / vnd die Finsternis habens nicht begriffen.')
```

The output and the return value should be as follows. Apart from `json` and `dataframe` the class may as well return other formats provided by the [CAB-webservice](https://kaskade.dwds.de/demo/cab/) e.g. `csv` (tabs), `text` (with vertical attributes), `raw` (just the normalized text), `ltwxml` (linguistic xml), `list` (just the normalized tokens):

### JSON

```Python
[
      {
         'word':'In',
         'lemma':'in',
         'pos':'APPR'
      },
      {
         'word':'ihm',
         'lemma':'er',
         'pos':'PPER'
      },
      {
         'word':'war',
         'lemma':'sein',
         'pos':'VAFIN'
      },
      {
         'word':'das',
         'lemma':'d',
         'pos':'ART'
      },
      {
         'word':'Leben',
         'lemma':'Leben',
         'pos':'NN'
      },
      {
         'word':'/',
         'lemma':'/',
         'pos':'$('
      },
      {
         'word':'und',
         'lemma':'und',
         'pos':'KON'
      },
      {
         'word':'das',
         'lemma':'d',
         'pos':'ART'
      },
      {
         'word':'Leben',
         'lemma':'Leben',
         'pos':'NN'
      },
      {
         'word':'war',
         'lemma':'sein',
         'pos':'VAFIN'
      },
      {
         'word':'das',
         'lemma':'d',
         'pos':'ART'
      },
      {
         'word':'Licht',
         'lemma':'Licht',
         'pos':'NN'
      },
      {
         'word':'der',
         'lemma':'d',
         'pos':'ART'
      },
      {
         'word':'Menschen',
         'lemma':'Mensch',
         'pos':'NN'
      },
      {
         'word':'/',
         'lemma':'/',
         'pos':'$('
      },
      {
         'word':'und',
         'lemma':'und',
         'pos':'KON'
      },
      {
         'word':'das',
         'lemma':'d',
         'pos':'ART'
      },
      {
         'word':'Licht',
         'lemma':'Licht',
         'pos':'NN'
      },
      {
         'word':'scheinet',
         'lemma':'scheinen',
         'pos':'VVFIN'
      },
      {
         'word':'in',
         'lemma':'in',
         'pos':'APPR'
      },
      {
         'word':'der',
         'lemma':'d',
         'pos':'ART'
      },
      {
         'word':'Finsternis',
         'lemma':'Finsternis',
         'pos':'NN'
      },
      {
         'word':'/',
         'lemma':'/',
         'pos':'$('
      },
      {
         'word':'und',
         'lemma':'und',
         'pos':'KON'
      },
      {
         'word':'die',
         'lemma':'d',
         'pos':'ART'
      },
      {
         'word':'Finsternis',
         'lemma':'Finsternis',
         'pos':'NN'
      },
      {
         'word':'habens',
         'lemma':'Habens',
         'pos':'NE'
      },
      {
         'word':'nicht',
         'lemma':'nicht',
         'pos':'PTKNEG'
      },
      {
         'word':'begriffen',
         'lemma':'begreifen',
         'pos':'VVPP'
      },
      {
         'word':'.',
         'lemma':'.',
         'pos':'$.'
      }
]
```

### DataFrame

You may as well let the class return a dataframe:

```Python
CAB = CabWrapper()
# Set the return format: json, text, csv, raw, ltwxml, dataframe
CAB.format = 'dataframe'
# Set the outputs you want (word, lemma, a/o pos), just concatenate them with pluses
CAB.output = 'word+lemma+pos'
# Query a text
CAB.getText('Jn jm war das Leben / vnd das Leben war das Liecht der Menschen / vnd das Liecht scheinet in der Finsternis / vnd die Finsternis habens nicht begriffen.')
```

The returned dataframe:

```text
           word       lemma     pos
0           In          in    APPR
1          ihm          er    PPER
2          war        sein   VAFIN
3          das           d     ART
4        Leben       Leben      NN
5            /           /      $(
6          und         und     KON
7          das           d     ART
8        Leben       Leben      NN
9          war        sein   VAFIN
10         das           d     ART
11       Licht       Licht      NN
12         der           d     ART
13    Menschen      Mensch      NN
14           /           /      $(
15         und         und     KON
16         das           d     ART
17       Licht       Licht      NN
18    scheinet    scheinen   VVFIN
19          in          in    APPR
20         der           d     ART
21  Finsternis  Finsternis      NN
22           /           /      $(
23         und         und     KON
24         die           d     ART
25  Finsternis  Finsternis      NN
26      habens      Habens      NE
27       nicht       nicht  PTKNEG
28   begriffen   begreifen    VVPP
29           .           .      $.
```

### CSV (Tabs)

```text
%% $s:lang=de
Jn	Jn	In	APPR	in
jm	jm	ihm	PPER	er
war	war	war	VAFIN	sein
das	das	das	ART	d
Leben	Leben	Leben	NN	Leben
/	/	/	$(	/
vnd	vnd	und	KON	und
das	das	das	ART	d
Leben	Leben	Leben	NN	Leben
war	war	war	VAFIN	sein
das	das	das	ART	d
Liecht	Liecht	Licht	NN	Licht
der	der	der	ART	d
Menschen	Menschen	Menschen	NN	Mensch
/	/	/	$(	/
vnd	vnd	und	KON	und
das	das	das	ART	d
Liecht	Liecht	Licht	NN	Licht
scheinet	scheinet	scheinet	VVFIN	scheinen
in	in	in	APPR	in
der	der	der	ART	d
Finsternis	Finsternis	Finsternis	NN	Finsternis
/	/	/	$(	/
vnd	vnd	und	KON	und
die	die	die	ART	d
Finsternis	Finsternis	Finsternis	NN	Finsternis
habens	habens	habens	NE	Habens
nicht	nicht	nicht	PTKNEG	nicht
begriffen	begriffen	begriffen	VVPP	begreifen
.	.	.	$.	.
```

### Text (with Annotations)

```text
%% $s:lang=de
Jn
	+[exlex] In
	+[errid] 68640
	+[xlit] l1=1 lx=1 l1s=Jn
	+[morph/safe] 0
	+[moot/word] In
	+[moot/tag] APPR
	+[moot/lemma] in
jm
	+[exlex] ihm
	+[errid] 65879
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=jm
	+[hasmorph] 1
	+[morph/safe] 1
	+[moot/word] ihm
	+[moot/tag] PPER
	+[moot/lemma] er
war
	+[exlex] war
	+[errid] 49126
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=war
	+[hasmorph] 1
	+[morph/safe] 1
	+[moot/word] war
	+[moot/tag] VAFIN
	+[moot/lemma] sein
das
	+[exlex] das
	+[errid] 24980
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=das
	+[hasmorph] 1
	+[morph/safe] 1
	+[moot/word] das
	+[moot/tag] ART
	+[moot/lemma] d
Leben
	+[exlex] Leben
	+[errid] ec
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=Leben
	+[hasmorph] 1
	+[morph/safe] 1
	+[moot/word] Leben
	+[moot/tag] NN
	+[moot/lemma] Leben
/
	+[xlit] l1=1 lx=1 l1s=/
	+[morph/safe] 1
	+[moot/word] /
	+[moot/tag] $(
	+[moot/lemma] /
vnd
	+[exlex] und
	+[errid] 9652
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=vnd
	+[morph/safe] 0
	+[moot/word] und
	+[moot/tag] KON
	+[moot/lemma] und
das
	+[exlex] das
	+[errid] 24980
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=das
	+[hasmorph] 1
	+[morph/safe] 1
	+[moot/word] das
	+[moot/tag] ART
	+[moot/lemma] d
Leben
	+[exlex] Leben
	+[errid] ec
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=Leben
	+[hasmorph] 1
	+[morph/safe] 1
	+[moot/word] Leben
	+[moot/tag] NN
	+[moot/lemma] Leben
war
	+[exlex] war
	+[errid] 49126
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=war
	+[hasmorph] 1
	+[morph/safe] 1
	+[moot/word] war
	+[moot/tag] VAFIN
	+[moot/lemma] sein
das
	+[exlex] das
	+[errid] 24980
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=das
	+[hasmorph] 1
	+[morph/safe] 1
	+[moot/word] das
	+[moot/tag] ART
	+[moot/lemma] d
Liecht
	+[exlex] Licht
	+[errid] 82068
	+[xlit] l1=1 lx=1 l1s=Liecht
	+[morph/safe] 0
	+[moot/word] Licht
	+[moot/tag] NN
	+[moot/lemma] Licht
der
	+[exlex] der
	+[errid] 57133
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=der
	+[hasmorph] 1
	+[morph/safe] 1
	+[moot/word] der
	+[moot/tag] ART
	+[moot/lemma] d
Menschen
	+[exlex] Menschen
	+[errid] ec
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=Menschen
	+[hasmorph] 1
	+[morph/safe] 1
	+[moot/word] Menschen
	+[moot/tag] NN
	+[moot/lemma] Mensch
/
	+[xlit] l1=1 lx=1 l1s=/
	+[morph/safe] 1
	+[moot/word] /
	+[moot/tag] $(
	+[moot/lemma] /
vnd
	+[exlex] und
	+[errid] 9652
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=vnd
	+[morph/safe] 0
	+[moot/word] und
	+[moot/tag] KON
	+[moot/lemma] und
das
	+[exlex] das
	+[errid] 24980
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=das
	+[hasmorph] 1
	+[morph/safe] 1
	+[moot/word] das
	+[moot/tag] ART
	+[moot/lemma] d
Liecht
	+[exlex] Licht
	+[errid] 82068
	+[xlit] l1=1 lx=1 l1s=Liecht
	+[morph/safe] 0
	+[moot/word] Licht
	+[moot/tag] NN
	+[moot/lemma] Licht
scheinet
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=scheinet
	+[hasmorph] 1
	+[morph/safe] 1
	+[moot/word] scheinet
	+[moot/tag] VVFIN
	+[moot/lemma] scheinen
in
	+[exlex] in
	+[errid] ec
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=in
	+[hasmorph] 1
	+[morph/safe] 1
	+[moot/word] in
	+[moot/tag] APPR
	+[moot/lemma] in
der
	+[exlex] der
	+[errid] 57133
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=der
	+[hasmorph] 1
	+[morph/safe] 1
	+[moot/word] der
	+[moot/tag] ART
	+[moot/lemma] d
Finsternis
	+[exlex] Finsternis
	+[errid] ec
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=Finsternis
	+[hasmorph] 1
	+[morph/safe] 1
	+[moot/word] Finsternis
	+[moot/tag] NN
	+[moot/lemma] Finsternis
/
	+[xlit] l1=1 lx=1 l1s=/
	+[morph/safe] 1
	+[moot/word] /
	+[moot/tag] $(
	+[moot/lemma] /
vnd
	+[exlex] und
	+[errid] 9652
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=vnd
	+[morph/safe] 0
	+[moot/word] und
	+[moot/tag] KON
	+[moot/lemma] und
die
	+[exlex] die
	+[errid] ec
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=die
	+[hasmorph] 1
	+[morph/safe] 1
	+[moot/word] die
	+[moot/tag] ART
	+[moot/lemma] d
Finsternis
	+[exlex] Finsternis
	+[errid] ec
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=Finsternis
	+[hasmorph] 1
	+[morph/safe] 1
	+[moot/word] Finsternis
	+[moot/tag] NN
	+[moot/lemma] Finsternis
habens
	+[lang] la
	+[xlit] l1=1 lx=1 l1s=habens
	+[morph/lat] [_FM][lat] <0>
	+[morph/safe] 1
	+[moot/word] habens
	+[moot/tag] NE
	+[moot/lemma] Habens
nicht
	+[exlex] nicht
	+[errid] ec
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=nicht
	+[hasmorph] 1
	+[morph/safe] 1
	+[moot/word] nicht
	+[moot/tag] PTKNEG
	+[moot/lemma] nicht
begriffen
	+[exlex] begriffen
	+[errid] ec
	+[lang] de
	+[xlit] l1=1 lx=1 l1s=begriffen
	+[hasmorph] 1
	+[morph/safe] 1
	+[moot/word] begriffen
	+[moot/tag] VVPP
	+[moot/lemma] begreifen
.
	+[exlex] .
	+[errid] ec
	+[xlit] l1=1 lx=1 l1s=.
	+[morph/safe] 1
	+[moot/word] .
	+[moot/tag] $.
	+[moot/lemma] .
```

### Raw Text

```text
In ihm war das Leben / und das Leben war das Licht der Menschen / und das Licht scheinet in der Finsternis / und die Finsternis habens nicht begriffen .
```

### ltwxml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<text>
 <s>
	<w lemma="in" pos="APPR" norm="In">Jn</w>
	<w lemma="er" pos="PPER" norm="ihm">jm</w>
	<w lemma="sein" pos="VAFIN" norm="war">war</w>
	<w lemma="d" pos="ART" norm="das">das</w>
	<w lemma="Leben" pos="NN" norm="Leben">Leben</w>
	<w lemma="/" pos="$(" norm="/">/</w>
	<w lemma="und" pos="KON" norm="und">vnd</w>
	<w lemma="d" pos="ART" norm="das">das</w>
	<w lemma="Leben" pos="NN" norm="Leben">Leben</w>
	<w lemma="sein" pos="VAFIN" norm="war">war</w>
	<w lemma="d" pos="ART" norm="das">das</w>
	<w lemma="Licht" pos="NN" norm="Licht">Liecht</w>
	<w lemma="d" pos="ART" norm="der">der</w>
	<w lemma="Mensch" pos="NN" norm="Menschen">Menschen</w>
	<w lemma="/" pos="$(" norm="/">/</w>
	<w lemma="und" pos="KON" norm="und">vnd</w>
	<w lemma="d" pos="ART" norm="das">das</w>
	<w lemma="Licht" pos="NN" norm="Licht">Liecht</w>
	<w lemma="scheinen" pos="VVFIN" norm="scheinet">scheinet</w>
	<w lemma="in" pos="APPR" norm="in">in</w>
	<w lemma="d" pos="ART" norm="der">der</w>
	<w lemma="Finsternis" pos="NN" norm="Finsternis">Finsternis</w>
	<w lemma="/" pos="$(" norm="/">/</w>
	<w lemma="und" pos="KON" norm="und">vnd</w>
	<w lemma="d" pos="ART" norm="die">die</w>
	<w lemma="Finsternis" pos="NN" norm="Finsternis">Finsternis</w>
	<w lemma="Habens" pos="NE" norm="habens">habens</w>
	<w lemma="nicht" pos="PTKNEG" norm="nicht">nicht</w>
	<w lemma="begreifen" pos="VVPP" norm="begriffen">begriffen</w>
	<w lemma="." pos="$." norm=".">.</w>
 </s>
</text>
```

### List

```Python
['In', 'ihm', 'war', 'das', 'Leben', '/', 'und', 'das', 'Leben', 'war', 'das', 'Licht', 'der', 'Menschen', '/', 'und', 'das', 'Licht', 'scheinet', 'in', 'der', 'Finsternis', '/', 'und', 'die', 'Finsternis', 'habens', 'nicht', 'begriffen', '.']
```
