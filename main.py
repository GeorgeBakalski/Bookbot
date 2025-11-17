from stats import  get_book_text
from stats import number_of_words
from stats import counting_characters

def main():
	text = get_book_text("books/frankenstein.txt")
	print (f"Found {number_of_words(text)} total words")
	chars = counting_characters(text)
	print (chars)
main()
