sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''

#
#   Maximum Likelihood Hypothesis
#
#
#   In this quiz we will find the maximum likelihood word based on the preceding word
#
#   Fill in the NextWordProbability procedure so that it takes in sample text and a word,
#   and returns a dictionary with keys the set of words that come after, whose values are
#   the number of times the key comes after that word.
#   
#   Just use .split() to split the sample_memo text into words separated by spaces.

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
