import math
import time 
import random

def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as 
    described in the handout for Project 3.
    '''
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    numerator = 0.0
    for i in vec1:
        for j in vec2:
            numerator += vec1[i] * vec2[j]
    denominator = norm(vec1) * norm(vec2)
    res = numerator/denominator
    return res 



def build_semantic_descriptors(sentences):
    d = {}
    print(sentences)
    for sentence in sentences:
        sentence = list(set(sentence))
        print("\n")
        print(sentence)
        print("\n")
        for word in sentence:
            print(word)
            if word != "":
                word = word.lower()
                if word not in d:
                    #Make a new dictionary inside the dictionary 
                    dic = {}
                    for word2 in sentence:
                        if word2 != word:
                            if word2 in dic:
                                #Upadate counts
                                dic[word2] += 1
                            else:
                                dic[word2] = 1
                        d[word] = dic
                #if word already been encountered
                else:
                    for word2 in sentence:
                        if word2 != word:
                            if word2 in d[word]:
                                d[word][word2] += 1 
                            else:
                                d[word][word2] = 1
    print(d)
    return d
    
def build_semantic_descriptors_from_files(filenames):
    '''This function takes a list of filenames of strings, which contains the names of files (the first one can
be opened using open(filenames[0], "r", encoding="latin1")), and returns the a dictionary of the
semantic descriptors of all the words in the files filenames, with the files treated as a single text.
You should assume that the following punctuation always separates sentences: ".", "!", "?", and that
is the only punctuation that separates sentences. You should also assume that that is the only punctuation
that separates sentences. Assume that only the following punctuation is present in the texts:
[",", "-", "--", ":", ";"]'''


    text = " "
    for file in range(len(filenames)):
        text += open(filenames[file], "r", encoding="latin1")
    #get valid lower case text 
        text = text.casefold()
        text += " "
    #Make it so all sentences end with a "."
    text = text.replace("!", ".")
    text = text.replace("?", ".")

    #Get rid of invalid punctuation 
    text = text.replace("\n", " ")
    text = text.replace(",", " ")
    text = text.replace("-", " ")
    text = text.replace("--", " ")
    text = text.replace(":", " ")
    text = text.replace(";", " ")
    
    #Split sentences 
    text = text.split('.')

    #start constructing the list of words we will send to the build function
    L = []
    for word in range(len(text) - 1):
        L.append(text[word].split(" "))

    for i in L:
        for j in i:
            if '' in i:
                i.remove('')

    return build_semantic_descriptors(L)




def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
   
    #make word lowercase 
    word = word.lower() 
    max_score = 0.0 

    #make choices lower case 
    for i in range(len(choices)):
        choices[i] = choices[i].lower()
    
    if word not in semantic_descriptors:
        #we need to guess 
        index = random.randint(0, len(choices))
        return choices[index]
    
    for choice in range(len(choices)):
        if choices[choice] not in semantic_descriptors:
            word_score = -1 
        else:
            word_score = similarity_fn(semantic_descriptors[word], semantic_descriptors[choices[choice]])
        if choice == 0:
            max = word_score 
            res = choices[choice]
        if word_score > max_score:
            max_score = word_score
            res= choices[choice]
        
        return res 
    
        


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
   score = 0.0
   file = ((open(filename, "r", encoding="latin1").read()).casefold()).split("\n")
   L = []
   for item in file:
    if item != "":
        L.append(item.split())
    for n in L:
       if most_similar_word(n[0], n[2:], semantic_descriptors, similarity_fn) == n[1]:
           score += 1 
    res = (score/len(L))*100
    return res
   

start = time.time()
sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt"])
res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
finish = time.time()
print(res, "of the guesses were correct")
print(finish - start)
