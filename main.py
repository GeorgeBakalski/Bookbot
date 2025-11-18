from stats import  get_book_text, number_of_words, counting_characters, make_list

def main():
	text = get_book_text("books/frankenstein.txt")
	chars = counting_characters(text)
	sorted_chars = make_list(chars)
	print ("============ BOOKBOT ============")
	print ("Analyzing book found at books/frankenstein.txt...")
	print ("----------- Word Count ----------")
	print (f"Found {number_of_words(text)} total words")
	print ("--------- Character Count -------")
	for entry in sorted_chars:
    		ch = entry["char"]
    		if ch.isalpha():
        		print(f"{ch}: {entry['num']}")
	print ("============= END ===============")


main()
