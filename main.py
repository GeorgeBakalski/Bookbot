from stats import  get_book_text, number_of_words, counting_characters, make_list
import sys

if len(sys.argv) != 2:
	print ("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def main():
	book_path = sys.argv[1]
	text = get_book_text(book_path)
	chars = counting_characters(text)
	sorted_chars = make_list(chars)
	print ("============ BOOKBOT ============")
	print (f"Analyzing book found at {book_path}...")
	print ("----------- Word Count ----------")
	print (f"Found {number_of_words(text)} total words")
	print ("--------- Character Count -------")
	for entry in sorted_chars:
    		ch = entry["char"]
    		if ch.isalpha():
        		print(f"{ch}: {entry['num']}")
	print ("============= END ===============")


main()
