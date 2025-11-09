from stats import get_num_words
from stats import get_char_count
from stats import generate_report
from stats import sort_on
import sys

def get_book_text(path_to_file):
 file_content=None
 print(f"Analyzing book found at {path_to_file}...")
 print(path_to_file)
 with open(path_to_file) as f:
    file_content = f.read()
    return file_content

def main():
 if len(sys.argv)!=2:
   print("Usage: python3 main.py <path_to_book>")
   sys.exit(1)

 path_to_file=sys.argv[1]
 print("============ BOOKBOT ============") 
 content=get_book_text(path_to_file)
 print("----------- Word Count ----------")
 wordCount = get_num_words(content)
 print(f"Found {wordCount} total words")
 char_dict=get_char_count(content)
 print("--------- Character Count -------")
 #print(char_dict)
 report_dict=generate_report(char_dict)
 for item in report_dict:
        #if not item["char"].isalpha():
        #    continue
        print(f"{item['char']}: {item['num']}")

 print("============= END ===============")
 #print(report_dict)
 # Using the special variable 
# __name__
if __name__=="__main__":
    main()