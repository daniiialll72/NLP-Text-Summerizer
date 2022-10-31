import re

class Sentence:
    def __init__(self, text, tag):
        self.text = text
        # tag: heading, subheading, paragraph
        self.tag = tag
        self.POS = 0
    
# read a text file
def read_file(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
    return text


# split text into sentences
def split_text(text):
    # split text into sentences
    sentences = sent_tokenize(text)
    return sentences


# define create_sentence function
def create_sentence(text, tag):
    text = text.strip()
    # split text into sentences
    sentences = text.split('.')
    # create a list of Sentence objects
    sentence_objects = []
    for sentence in sentences:
        sentence_objects.append(Sentence(sentence, tag))
    return sentence_objects

# define sent_tokenize function
# this function will use html tags to split text into sentences
# and the sentences are separated by period.
def sent_tokenize(text):
    # split text into sentences
    sentences = []
    # split text into paragraphs based on html tags
    # regex to find text between <h1> and </h1> including whitespace
    # or regex to find text between <p> and <p> including whitespace
    # pattern = re.compile(r'(<h1>(.*?)</h1>)|(<p>.*?</p>)', re.DOTALL)
    pattern = re.compile(r'<h1>(.*?)<\/h1>|<h2>(.*?)</h2>|<p>(.*?)<\/p>', re.DOTALL)
    # pattern = re.compile(r'<h1>(.*?)<\/h1>')
    # find all matches
    matches = pattern.finditer(text)
    # loop through matches
    for match in matches:   
        # get the text between html tags
        # if the match is a heading
        if match.group(1):
            # get the text between <h1> and </h1>
            text = match.group(1)
            # set tag to heading
            tag = 'heading'
            # create a list of Sentence objects
            sentence_objects = create_sentence(text, tag)
            # add the list of Sentence objects to sentences
            sentences.extend(sentence_objects)
        # match h2
        elif match.group(2):
            text = match.group(2)
            tag = 'heading 2'
            sentence_objects = create_sentence(text, tag)
            sentences.extend(sentence_objects)


        # if the match is a paragraph
        else:
            # get the text between <p> and </p>
            text = match.group(3)
            # set tag to paragraph
            tag = 'paragraph'
            # create a list of Sentence objects
            sentence_objects = create_sentence(text, tag)
            # add the list of Sentence objects to sentences
            sentences.extend(sentence_objects)

    # print all the sentences
    for sentence in sentences:
        print("structure: %s, Text: %s" %( sentence.tag, sentence.text.strip()))

    return sentences
    

if __name__ == "__main__":
    # read a text file
    text = read_file('dataset/finland.html')
    # split text into sentences
    sentences = split_text(text)
