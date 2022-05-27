# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename,'r') as file_to_be_read:
        file_contents = file_to_be_read.read()
        return file_contents
read_file_content('story.txt')

def count_words():
    text = read_file_content('story.txt')
    # [assignment] Add your code here
    text = text.replace('?',"")
    text = text.replace(',',"")
    text = text.replace('.',"")
    text = text.lower()
    text = text.strip()
    wordstring = text.split()
    
    wordfreq = []
    for eachword in wordstring:
        wordfreq.append(wordstring.count(eachword))
    print(dict(list(zip(wordstring,wordfreq))))
count_words()