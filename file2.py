def main():
	ls1 = [1, 2, 3, 4, 5]
	ls2 = [4, 5, 6, 7, 8]
	elements_in_both = []
	for element in ls1:
  		if element in ls2:
   		elements_in_both.append(element)
	print(elements_in_both)