clue = "So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?"

def main():
    words = clue.replace('?','').replace(',','').split(' ')
    print 'count of word: ', len(words)

    word_freq = {}
    for word in words:
        word_freq[word.upper()] = words.count(word)
    print word_freq

    print word_freq['you'.upper()]
    print word_freq['if'.upper()]


if __name__ == '__main__':
    main()