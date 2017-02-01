#------------------------------------------------------------------

#
#   Bayes Optimal Classifier
#
#   In this quiz we will compute the optimal label for a second missing word in a row
#   based on the possible words that could be in the first blank
#
#   Finish the procedurce, LaterWords(), below
#
#   You may want to import your code from the previous programming exercise!
#

sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''

corrupted_memo = '''
Yeah, I'm gonna --- you to go ahead --- --- complain about this. Oh, and if you could --- --- and sit at the kids' table, that'd be --- 
'''

data_list = sample_memo.strip().split()

words_to_guess = ["ahead","could"]


def NextWordProbability(sampletext,word):
    normalized_sampletext = sampletext.lower().replace('\'',' ').replace('?',' ').replace(':',' ').replace(',',' ').replace('\n',' ').replace('.',' ').split(' ')
    word = word.lower()

    afterWordFreq = {}
    for i in range(0,len(normalized_sampletext)-1,1):
        if normalized_sampletext[i] != word:
            continue

        curWord = normalized_sampletext[i]
        laterWord = normalized_sampletext[i+1]

        if curWord == word and not afterWordFreq.has_key(laterWord):
            afterWordFreq[laterWord] = 0
            index_list = [idx for idx in range(i, len(normalized_sampletext),1) if normalized_sampletext[idx]==curWord ]
            for idx in index_list:
                if normalized_sampletext[idx+1] == laterWord:
                    afterWordFreq[laterWord] += 1
    
    return afterWordFreq

def LaterWords(sample,word,distance):
    '''@param sample: a sample of text to draw from
    @param word: a word occuring before a corrupted sequence
    @param distance: how many words later to estimate (i.e. 1 for the next word, 2 for the word after that)
    @returns: a single word which is the most likely possibility
    '''
    
    # TODO: Given a word, collect the relative probabilities of possible following words
    # from @sample. You may want to import your code from the maximum likelihood exercise.
    dictNextWord = NextWordProbability(sample,word)

    # TODO: Repeat the above process--for each distance beyond 1, evaluate the words that
    # might come after each word, and combine them weighting by relative probability
    # into an estimate of what might appear next.

    dictNextWord2 = {}
    for key in dictNextWord.keys():
        freq = NextWordProbability(sample, key)
        dictNextWord2[key] = sorted(freq, key=freq.get, reverse=True)        # how to extract the key which has max value using lambda function


    if distance == 1:
        return sorted(dictNextWord, key=dictNextWord.get, reverse=True)[0]
    elif distance == 2:
        firstWord = sorted(dictNextWord, key=dictNextWord.get, reverse=True)[0]
        return dictNextWord2[firstWord][0]

    return {}

if __name__ == '__main__':
    print LaterWords(sample_memo,"gonna",1)    
    print LaterWords(sample_memo,"ahead",1)
    print LaterWords(sample_memo,"ahead",2)
    print LaterWords(sample_memo,"could",1)
    print LaterWords(sample_memo,"could",2)
    print LaterWords(sample_memo,"be",1)
    print LaterWords(sample_memo,"go",1)
    print LaterWords(sample_memo,"go",2)
    print LaterWords(sample_memo,"could",1)
    