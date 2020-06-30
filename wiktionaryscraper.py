from wiktionaryparser import WiktionaryParser
import time
import json

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


def main():
    dictionary = []

    file = open("conjugated_words.txt", "r")
    lines = file.readlines()

    step = 0
    percent = 0
    for line in lines:
        word = line.rstrip()
        try:
            json_entry = generate_json_entry(word)
        except:
            pass
        dictionary.append(json_entry)
        step  += 1
        if step % 220 == 0:
            percent += 1
            file2 = open("tagalog_dictionary.txt", "w", encoding="utf-8")
            json.dump(dictionary, file2, ensure_ascii=False)
            print ("Percentage: " + str(percent))
            print ("Step: " + str(step))
            file2.close()

    file.close()
    print ("Finnished")

main()




