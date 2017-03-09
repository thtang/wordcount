import nltk
from nltk.corpus import stopwords
text = open('building_global_community.txt').read()
words = nltk.tokenize.word_tokenize(text)
# filter out symbols
words = [word for word in words if word.isalpha()]

# normalize words and count
words = [word.lower() for word in words]

#filter out the stop word
nltk.download('stopwords')
stopwords = set(stopwords.words('english'))
words = [word for word in words if word not in stopwords]

#count the occurance of words
wordCounter = nltk.FreqDist(words)

print (wordCounter.most_common(20))

####Bonus
nltk.FreqDist(nltk.pos_tag(words)).items()
POS_wordcount = {}

for i in nltk.FreqDist(nltk.pos_tag(words)).items():
    if i[0][1] in POS_wordcount:
        POS_wordcount[i[0][1]].update({i[0][0]:i[1]})
    else:
        POS_wordcount[i[0][1]] = {}
        POS_wordcount[i[0][1]].update({i[0][0]:i[1]})

print (POS_wordcount["NN"]["community"])
