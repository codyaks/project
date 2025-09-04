class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+' -( '+self.meaning+' ) '
flash=[]
print("welcome to the flashcard application")
while True:
    word_in=input("please enter the word you like to add-")
    meaning_in=input("please enter the meaning of word-")
    flash.append(flashcard(word_in,meaning_in))
    comti=int(input("to add more words enter 0 to exit enter 1-"))
    if(comti):
        break
for i in flash:
    print("**",i)