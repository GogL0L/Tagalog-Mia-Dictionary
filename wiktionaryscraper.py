from wiktionaryparser import WiktionaryParser
import time

# parser = WiktionaryParser()
# word = parser.fetch('manok','tagalog')
# t0 = time.time()
# print(word[0]['definitions'][0]['partOfSpeech'])
# t1 = time.time()
# print ("time: " + str(t1-t0))

def getPos(entry):
    result = entry[0]['definitions'][0]['partOfSpeech']
    if result == "" or None:
        return "n/a"
    else:
        return result

def getPron(entry):
    result_list = entry[0]['pronunciations']['text']
    if result_list != []:
        return result_list[0]
    else:
        return "n/a"

def getDef(entry):
    result_list = entry[0]['definitions'][0]['text']
    if result_list != []:
        return ",\n".join(result_list)
    else:
        return "n/a"

def getAudio(entry):
    result_list = entry[0]['pronunciations']['audio']
    if result_list != []:
        return result_list[0]
    else:
        return "n/a"

def getEx(entry):
    result_list = entry[0]['definitions'][0]['examples']
    if result_list != []:
        return ",\n,".join(result_list)
    else:
        return "n/a"

def getRelated(entry):
    result = entry[0]['definitions'][0]['relatedWords']
    return result




# print('pos:')
# print(getPos(word))
# print('\n pronunciations:')
# print(getPron(word))
# print('\n definitions:')
# print(getDef(word))
# print('\n audio:')
# print(getAudio(word))
# print('\n examples:')
# print(getEx(word))
# print('\n relatedWords:')
# print(getRelated(word))



def generate_json_entry(entry_word):
    parser = WiktionaryParser()
    word = parser.fetch(entry_word,'tagalog')
    json_entry = {"term":entry_word,
                  "altterm":"",
                  "pronunciation": getPron(word),
                  "definition":getDef(word),
                  "pos":getPos(word),
                  "examples":getEx(word),
                  "audio":getAudio(word)}
    return json_entry

# print (generate_json_entry("manok"))

def main():
    dictionary = []

    file = open("conjugated_words.txt", "r")
    lines = file.readlines()
    for x in (0,4):
        word = lines[x].rstrip()
        json_entry = generate_json_entry(word)
        dictionary.append(json_entry)
    file.close()

    file2 = open("tagalog_dictionary.txt", "w", encoding="utf-8")
    json.dump(dictionary, file2, ensure_ascii=False)
    file2.close()
    return 1




