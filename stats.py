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

def counting_characters(f):
	lower_case = f.lower()
	letters = {}
	for ch in lower_case:
		if ch not in letters:
			letters[ch] = 1
		else:
			letters[ch] += 1
	return letters

def sort_on(entry):
	return entry["num"]

def make_list (f):
	list_of_chars = []
	for key, count in f.items():
		list_of_chars.append({"char": key, "num": count})
	list_of_chars.sort(reverse=True, key=sort_on)
	return list_of_chars
