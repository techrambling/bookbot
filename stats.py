def get_num_words(content):
 wordList=content.split()
 wordCount=len(wordList)
 return wordCount 


def get_char_count(content):
    char_dict={}
    for i in range(0, len(content)):
        #print(content[i].lower())
        value = content[i].lower()
        #print(value)
        if value in char_dict and value is not None:
            #print(f"value exist {value} in dictionary.")
            char_dict[value]+=1           
        else:
            #print(f"value doest not exist {value} in dictionary.")
            char_dict[value]=1

    return char_dict

def sort_on(items):
        return items["num"]

def generate_report(char_dict):        
    #result_list=[]
        #result_dict={}
    sorted_list = []
    for ch in char_dict:
        if ch.isalpha():
          sorted_list.append({"char": ch, "num": char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
                

  
  