# Audible file to mp3 files for each chapter

Audio books from Audible (AAX files) can only be played using software provided by Audible. Customers who do not convert them to a more open format like mp3 are likely to lose the ability to listen to their audio books at some point in the future. Converting an audio book to one long mp3 file is relatively easy. These scripts help with the more tedious task of splitting it into chapters.

A video showing the steps can be found [on Youtube](https://www.youtube.com/watch?v=oztnCJlY3bo).

## requirements

* a converter like aax2mp3 and an Audible player (works on Windows or Mac, might work with Wine on Linux)

* [Audacity](https://en.wikipedia.org/wiki/Audacity_%28audio_editor%29)

* the console program [mp3splt](http://mp3splt.sourceforge.net/mp3splt_page/documentation/man.html)

This works on Linux. Small changes may be necessary for other operating systems.

## usage

* use a program like aax2mp3 to create the long mp3

* create a working folder (This is where all the following steps happen.)

* move the long mp3 there and call it `uncut.mp3`

* put `audible_to_audacity.py` and `audacity_to_mp3splt.py` there

* copy the chapter list from Audible to `audible_chapters.txt`

* (adapt the regex in `audible_to_audacity.py` if the lines in your chapter list look different)

* run `audible_to_audacity.py`, which will create `audacity_labels_in.txt`

* (If you are fine with the makeshift chapter names and the times in that file, you could just skip the Audacity part, and rename it to `audacity_labels_out.txt`.)

* open `uncut.mp3` in Audacity and import the labels in `audacity_labels_in.txt`

* modify chapter names and times as you wish (Make sure to enter names that will sort the files in the correct order. This usually requires starting the file name with a number - starting with leading zeros if necessary.)

* export the labels as `audacity_labels_out.txt`

* run `audacity_to_mp3splt.py`

This creates a folder with mp3 files for the chapters. The names are like they were entered in Audacity.

## _War and Peace_ example

The example of `audacity_labels_out.txt` is for the 61 hour recording of _War and Peace_ (translated by Garnett, read by Davidson). For this book the times from the chapter table are not much help. In the Audacity screenshot it can be seen, that the start label for chapter 4 in part 9 is five minutes before the actual start on the right of the image.

![audacity screenshot](http://paste.watchduck.net/1709/war_and_peace_audacity.png)

## adapting to changes by Audible

Audible makes occasional changes, so some tinkering may be required to adapt.

A small change was, that at some point there were line breaks in the chapter list.
That can be fixed with a little [regex](https://en.wikipedia.org/wiki/Regular_expression) magic:
Replace `Chapter (\d+)\n(\d)` by `Chapter \1\t\2`.
(See [screenshot](http://paste.watchduck.net/1812/gedit_regex.png). [Gedit](https://en.wikipedia.org/wiki/Gedit) uses `\1` and `\2` for the groupings. Other editors may use `$1` and `$2`.)

A more important and annoying change is, that the chapter list now (December 2018) shows chapter lenghts instead of absolute times.
[`audible_to_audacity.py`](https://github.com/watchduck/split_audiobooks/blob/master/audible_to_audacity.py)
was changed accordingly.
([This](https://github.com/watchduck/split_audiobooks/blob/56dfac2dfeae9897563ed421cec02e5981258a1c/audible_to_audacity.py)
is the former version.)
But the half second gap is only approximate. To find the exact beginning for each chapter it is necessary to manually adapt each label in Audacity. This is tedious, but at the right zoom level it is easy to visually identify the gaps between chapters.
