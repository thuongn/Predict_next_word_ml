def NextWordProbability(sampletext,word):
    ssplit = sampletext.split(" ")
    preceding_word = []
    freq = []
    rtn = {}
    for i in range (1,len(ssplit)):
        if ssplit[i]==word:
            if (ssplit[i+1] in rtn):
                rtn[ssplit[i+1]] = rtn[ssplit[i+1]] + 1
            else:
                rtn[ssplit[i+1]] = 1 
    return rtn