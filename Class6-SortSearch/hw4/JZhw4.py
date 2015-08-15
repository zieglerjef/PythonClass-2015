# insertion sort
def insertion_sort(item_list):	
	for i in range(1, len(item_list)):
		k = item_list[i]
		j = i - 1
		while (j >= 0) and (item_list[j] > k):
			item_list[j+1] = item_list[j]
			j = j - 1
		item_list[j+1] = k
	print(item_list)
		
# selection sort
def selection_sort(item_list):
	for spot in range(len(item_list)-1,0,-1):
		positionOfMax=0
		for location in range(1, spot + 1):
			if item_list[location] > item_list[positionOfMax]:
				positionOfMax = location
			temp = item_list[spot]
			item_list[spot] = item_list[positionOfMax]
			item_list[positionOfMax] = temp
	print(item_list)