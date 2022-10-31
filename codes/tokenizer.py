from unittest import result
import nltk
import sklearn
import re
# nltk.download ()
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

stopwords.words('english')

class tokenizer:
    def __init__(self, word, sentence):
        self.word = word
        self.sentence = sentence


def get_tokenized_sentence(data):
    sentences = sent_tokenize(data)
    return sentences


def get_tokenized_words(data):
    words = word_tokenize(data)
    return words


def remove_stop_words(data):
    data = re.sub('[^a-zA-Z]', ' ', data)
    data = data.lower()
    data = data.split()
    data = [word for word in data if not word in set(
        stopwords.words('english'))]
    data = ' '.join(data)
    return data

# Lemmatization approach
# Stemming with lemmatization to get proper meaning words after stemming
def lemmatizer(sentences):
    # create lemmatize object
    lemmmatizer = WordNetLemmatizer()
    # get sentences
    for i in range(len(sentences)):
        words = word_tokenize(sentences[i])
        # List comprehension
        words = [lemmmatizer.lemmatize(
            word.lower()) for word in words if word not in set(stopwords.words('english'))]
        sentences[i] = ' '.join(words)
    return sentences

def TfidfVectorizor(sentence):
    cv=TfidfVectorizer()
    x=cv.fit_transform(sentence)
    return x

# Sample Paragraph : Information about Manav Project
# data = "Recent times have witnessed an explosion in the amount of biological data generated. There are millions of research articles with pivotal information on human health and disease, spanning from single molecule resolution to the level of the whole organism. However, this information is scattered in different databases, repositories and in the text of journal articles. This makes the seamless extraction of scientific information an extremely challenging and time-consuming (yet incomplete) process. With 100+ databases and millions of data points (combined) from just human cells/tissue and disease, there is a pressing need to collate this information in such a way that users like academic/industrial/clinical researcher as well as teachers and students can easily access information that is relevant to them from a common and modular platform. Although there are ambitious ongoing efforts like the Recon X, The Virtual Physiological Human, Human Cell Atlas, none of these projects aim to build the map of the whole human body simultaneously comparing both macro(organ/tissue/cell) and micro (molecular interaction networks) level details. Manav-Human Atlas Initiative aims to construct a comprehensive map of the entire human body which will explicitly document macro to micro level information. The project Manav will dramatically accelerate our understanding of the working of the human body and help design better therapeutic targets for treating diseases like cancer, diabetes and more. This project will require understanding, extracting and collating information from millions of scientific papers which would need a massive investment of time, effort and manpower. The large pool of scientifically literate population in India pursuing a bachelors /masters / Ph.D. is a great resource that will be trained and engaged as part of this project to use the annotation tool being developed to collate, curate, manage and visualize this scientific information. This project is funded by Department of Biotechnology (DBT), Government of India as a collaboration between Persistent Systems, NCCS and IISER, Pune."
data = "finland is a nordic country and the capital is Helsinki. finland is big. finland is beautiful. "
sentences = get_tokenized_sentence(data)
# print(sentences)
output = lemmatizer(sentences)

print(output)
# for sent in output:
res = TfidfVectorizor(output)
# print(res.get_feature_names_out())
# print(res[0])

score_1 = 0
for i in res[0]:
    print(i.data)
    score_1 += i
    
# print('Score sentence 1 is %s' %score_1)

# print(res)

# print(output)