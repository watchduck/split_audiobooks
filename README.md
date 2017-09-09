# Audible file to mp3 files for each chapter

Audio books from Audible (AAX files) can only be played using software provided by Audible. Customers who do not convert them to a more open format like mp3 are likely to lose the ability to listen to their audio books at some point in the future. Converting an audio book to one long mp3 file is relatively easy. These scripts help with the more tedious task of splitting it into chapters.

## requirements

* a converter like aax2mp3 and an Audible player (works only on Windows or Mac)

* [Audacity](https://en.wikipedia.org/wiki/Audacity_%28audio_editor%29)

* the console program [mp3splt](http://mp3splt.sourceforge.net/mp3splt_page/documentation/man.html)

This works on Linux. Small changes may be necessary for other operating systems.

## usage

* use a program like aax2mp3 to create the long mp3

* create a working folder (This is where all the following steps happen.)

* move the long mp3 there and call it `uncut.mp3`

* put `audible_to_audacity.py` and `audacity_to_mp3splt.py` there

* copy the chapter list from Audible to `audible_chapters.txt`

* run `audible_to_audacity.py`, which will create `audacity_labels_in.txt`

* (If you are fine with the makeshift chapter names and the times in that file, you could just skip the Audacity part, and rename it to `audacity_labels_out.txt`.)

* open `uncut.mp3` in Audacity and import the labels in `audacity_labels_in.txt`

* modify chapter names and times as you wish (Make sure to enter names that will sort the files in the correct order. This usually requires starting the file name with a number - starting with leading zeros if necessary.)

* export the labels as `audacity_labels_out.txt`

* run `audacity_to_mp3splt.py`

This creates a folder with mp3 files for the chapters. The names are like they were entered in Audacity.
