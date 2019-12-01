import random
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
sp = spacy.load('en_core_web_sm')

f = open('moby-dick.txt','r')
novel = f.read()

passages = novel.split('\n\n')

passageNumber = 0
twee = ''

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
    finally:    
        p = p.replace(link1, '[[' + link1 + '->' + str(random.randint(1,2462)) + ']]', 1)
        p = p.replace(link2, '[[' + link2 + '->' + str(random.randint(1,2462)) + ']]', 1)
        p = p.replace(link3, '[[' + link3 + '->' + str(random.randint(1,2462)) + ']]', 1)
        passageNumber = passageNumber + 1   
        p = ":: " + str(passageNumber) + '\n' + p + '\n\n'
        twee = twee + p

# cleanup = re.compile(r"]]->\d+]]")
# twee = cleanup.sub()

n = open("src/tarred_twine.twee","w")
n.write(twee)
n.close()