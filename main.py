##Read in book from different txt file for training data
##The function return a big string with all of the book append one after another
def readin_training_data():
    import os.path
    fcontent = ""
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "TrainingData/2city10.txt")
    with open(path, 'r') as content_file:
        content = content_file.read()
    fcontent = fcontent + content

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "TrainingData/2city11.txt")
    with open(path, 'r') as content_file:
        content = content_file.read()
    fcontent = fcontent + content

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "TrainingData/7gabl10.txt")
    with open(path, 'r') as content_file:
        content = content_file.read()
    fcontent = fcontent + content

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "TrainingData/80day10.txt")
    with open(path, 'r') as content_file:
        content = content_file.read()
    fcontent = fcontent + content

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "TrainingData/2000010.txt")
    with open(path, 'r') as content_file:
        content = content_file.read()
    fcontent = fcontent + content

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "TrainingData/abbott-flatland-361.txt")
    with open(path, 'r') as content_file:
        content = content_file.read()
    fcontent = fcontent + content

    return fcontent

## this fucntion return the list of the next word with the proabbility of it given a word
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
    tsum = sum(rtn.values())
    for key, value in rtn.items():
        rtn[key] = rtn[key]*1.00 / tsum
    return rtn

print NextWordProbability(readin_training_data(),"win")