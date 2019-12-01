# An End of Tarred Twine
[An End of Tarred Twine](https://fugitivetexts.net/tarredtwine/index.html) is a randomly generated Twine hypertext version of _Moby Dick_. It's interactive and nonlinear and serendipitously fun. But good luck following the story!

I created this Twine version of _Moby Dick_ for National Novel Generation Month (NaNoGenMo) 2019. The heart of the project is a Python program that breaks Herman Melville's 1851 masterpiece into 2,463 indiviudual Twine passages. Next, the program uses the SpaCy natural language processing module to identify several named entities and verbs in each passage, and then link them randomly to one of the other over 2,463 passages. The program generates a twee file (twee being the equivalent of Twine markup). Finally, I use the command line compiler Tweego to generate the actual Twine HTML file.  

Necessary components are:
* A cleaned up unicode text version of Moby Dick
* Python with the regex, random, and spaCy modules
* Tweego
* Plus, I did some cleanup of the final twee code in Notepad++.

Some stats:
* 250,051 words
* 2463 passages (or nodes)
* 6476 links between the passages
* 2.63 average links on any single passage

Screenshot:

![Title Page for An End of Tarred Twine](https://github.com/samplereality/tarred-twine/blob/master/tarredTwineCover.png)
