# Load up the various Python modules we need. The most important here is spaCy, a natural language processing framework.
import random
import spacy
import re
from spacy.lang.en.stop_words import STOP_WORDS
sp = spacy.load('en_core_web_sm')

# Next open up a text file version of Moby Dick
f = open('moby-dick.txt','r')
novel = f.read()

# Now we're going to split the novel into distinct passages, or nodes, with every paragraph becoming a single node. That will add up to 2,463 passages!
passages = novel.split('\n\n')

# Defining a few variables
passageNumber = 0
twee = ''

# Here's the heart of the program. For each passage, the program finds two or three words to turn into hyperlinks that lead to another one of the 2,463 passages. Links will either be nouns or noun phrases identified by spaCy's entity recognition abilities, verb identified by spaCy, or if those fail, simply random words in each passage (not including common 'stopwords' like 'a' and 'the.')
for p in passages:
    try:
        sen = sp(p)
        link1 = (sen.ents[0])
        link1 = str(link1)
        link2 = (sen.ents[-1])
        link2 = str(link2)
        verbs = set()
        for word in sen:
            if word.pos_ == "VERB":
                verbs.add(word)
                links = random.sample(verbs, len(verbs))
                link3 = str(random.choice(links))
    except IndexError:
        words = p.split(' ')
        filtered_words = [word for word in words if word not in STOP_WORDS]
        link1 = random.choice(filtered_words)
        # filtered_words.remove(link1)
        link2 = random.choice(filtered_words)
        verbs = set()
        sen = sp(p)
        for word in sen:
            if word.pos_ == "VERB":
                verbs.add(word)
                links = random.sample(verbs,len(verbs))
                link3 = str(random.choice(links))
# The next few lines replace the words randomly selected as links with twee notation (the markup that Twine generates) that direct those links to random passages. All told, there are 6,476 links in the finished work. This section also names each passage using Twine notation.                 
    finally:    
        p = p.replace(link1, '[[' + link1 + '->' + str(random.randint(1,2462)) + ']]', 1)
        p = p.replace(link2, '[[' + link2 + '->' + str(random.randint(1,2462)) + ']]', 1)
        p = p.replace(link3, '[[' + link3 + '->' + str(random.randint(1,2462)) + ']]', 1)
        passageNumber = passageNumber + 1   
        p = ":: " + str(passageNumber) + '\n' + p + '\n\n'
        twee = twee + p

# If the same word is chosen twice in the same passage as a link, the twee notation gets missed up. This regex will clean up the mistakes.
cleanup = re.compile(r"]]->\d+]]")
twee = cleanup.sub()

# Finally, write the twee code to a file. Next, use the command line compiler tweego to turn the twee code into a Twine HTML file.
n = open("src/tarred_twine.twee","w")
n.write(twee)
n.close()
