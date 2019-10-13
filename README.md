# python-wrapper-cab-webservice
Small Python wrapper class for the CAB-webservice.

This class provides a simple interface to interact with B. Jurish’s [CAB-webservice](https://kaskade.dwds.de/demo/cab/) from within Python.

## CAB-webservice
For more information about the CAB-webservice please see:

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

The output and the return value should be as follows:

```Python
[
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
]
```

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
