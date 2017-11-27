"""
1. read book text (txt,ansi)[path-input]
2. split txt into words, make a list of words
3. strip whitespaces and punctuation
4. make a list of unique words
5. count word occurences, create dictionary: {word : counter}

...
6.
7.


"""
class Book:
    def __init__(self, path):
        self.read(path)

    def read(self,path):
        with open(path,'r') as f:
            self.words=[word.strip(' \'.,"/-!?&():;')
                        for line in f
                        for word in line.lower().strip().split()
                        ]
        
