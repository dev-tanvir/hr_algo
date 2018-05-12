""" 
Algorithms > sorting > big sorting

"""
# Complete the bigSorting function below.
def bigSorting(unsorted):
    #unsorted.sort()
    #sorted_list = []
    #for i in unsorted:
    #    sorted_list.append(str(i))
    #return sorted_list
    
    # ^ it gets timeout error!!!!
		
    unsorted.sort(key=int)            # key=int is "key" here, pun intended
    list_sort = []
    for i in unsorted:
        list_sort.append(i)
    return list_sort



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    unsorted = []

    for _ in range(n):
        #unsorted_item = int(input())
	unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

