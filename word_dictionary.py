# have a python dictionary that has a key/ value pair that represent a word and its defination
# collect input from user , input is a word
# check if the word is in the dictionary
# print the defination



from PyDictionary import PyDictionary
dictionary = PyDictionary()

while True:
    word = input("Enter your word: ")
    if word == "":
        break
    
    print(dictionary.meaning(word))


""" def main():
    word_dictionary ={
        'hi': 'a way of greeting',
        'eyes':'an organ for seeing',
        'earth':'a planet in space',
    } 

    while True:

        word=input("enter your word: ")
        if word=="":
            break
        if word in word_dictionary:
            print(word, ":", word_dictionary[word])

main()
  """

  