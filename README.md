# Audible file to mp3 files for each chapter

Audio books from Audible (AAX files) can only be played using software provided by Audible. Customers who do not convert them to a more open format like mp3 are likely to lose the ability to listen to their audio books at some point in the future. Converting an audio book to one long mp3 file is relatively easy. These scripts help with the more tedious task of splitting it into chapters.

A video showing the steps can be found [on Youtube](https://www.youtube.com/watch?v=oztnCJlY3bo).

In the video the initial conversion is done with aax2mp3 and the Audible player on Windows.<br>
Meanwhile (2019) [OpenAudible](https://openaudible.org/) may be a better choice. It works on all platforms, including Linux.

## requirements

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

* [Audacity](https://en.wikipedia.org/wiki/Audacity_%28audio_editor%29)

* the console program [mp3splt](http://mp3splt.sourceforge.net/mp3splt_page/documentation/man.html)

This works on Linux. Small changes may be necessary for other operating systems.

(In [`audacity_to_mp3splt.py`](https://github.com/watchduck/split_audiobooks/blob/master/audacity_to_mp3splt.py)
spaces encoded as `'\ '` are used in a command.<br>
If your OS complains about that, change `name_spaces` accordingly.)

## usage

* create the uncut mp3

* create a working folder (This is where all the following steps happen.)

* move the uncut mp3 there and call it `uncut.mp3`

* put `audible_to_audacity.py` and `audacity_to_mp3splt.py` there

* copy the chapter list from Audible to `audible_chapters.txt` (keeping only the chapter names and times)

* run `audible_to_audacity.py`, which will create `audacity_labels_in.txt`

* open `uncut.mp3` in Audacity and import `audacity_labels_in.txt`

* modify chapter names and times as you wish (The default chapter names are numbers with leading zeros. If you remove them, make sure to add other prefixes that sort the files in the correct order.)

* export the labels as `audacity_labels_out.txt`

* run `audacity_to_mp3splt.py`

This creates a folder with mp3 files for the chapters. The file names are like they were entered in Audacity, but with the spaces replaced by underscores. For the title tags the names with spaces are used.

## _War and Peace_ example

The example file [`audacity_labels_out.txt`](https://github.com/watchduck/split_audiobooks/blob/master/audacity_labels_out_example.txt) is for the 61 hour recording of _War and Peace_ (translated by Garnett, read by Davidson). For this book the times from the chapter table are not much help. In the Audacity screenshot it can be seen, that the start label for chapter 4 in part 9 is five minutes before the actual start on the right of the image.

![audacity screenshot](http://paste.watchduck.net/1709/war_and_peace_audacity.png)

## adapting to changes by Audible

Audible makes occasional changes, so some tinkering may be required to adapt. A small change was, that at some point there were line breaks in the chapter list. A more important and annoying change is, that the chapter list now (2019) shows chapter lenghts instead of absolute times.
[`audible_to_audacity.py`](https://github.com/watchduck/split_audiobooks/blob/master/audible_to_audacity.py)
was changed accordingly from the
[former version](https://github.com/watchduck/split_audiobooks/blob/56dfac2dfeae9897563ed421cec02e5981258a1c/audible_to_audacity.py).
It now expects `audible_chapters.txt` to look like this for two chapters of 2 and 1.5 minutes:

    Chapter 1
    00:02:00
    Chapter 2
    00:01:30

The script adds the chapter lengths together and assumes half second gap between the chapters, but this is only approximate. To find the exact beginning for each chapter it is necessary to manually adapt each label in Audacity. This is tedious, but at the right zoom level it is easy to visually identify the gaps between chapters.

The chapter names provided by Audible are almost always just like "Chapter 1". They are ignored by the script, and numbers with leading zeros are generated as new chapter names. E.g. `000` for the intro and `001` the first chapter. An integer can be passed to the script as a parameter to increase or reduce these numbers:

    $ python audible_to_audacity.py 1
