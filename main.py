def get_book_text(a):
	with  open(a) as f:
		file_contents = f.read()
	return file_contents

def number_of_words(f):
	words = f.split()
	count = 0
	for word in words:
		count +=1
	return count

def main():
	text = get_book_text("books/frankenstein.txt")
	print (f"Found {number_of_words(text)} total words")

main()
