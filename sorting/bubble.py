# Bubble sort
## - Swap adjacent elements if they're not in correct order

def bubble_sort(lst):
  """
  Bubble sort function
  :param lst: list of unsorted integers
  """

  for i in range(len(lst)):
    for j in range(0,len(lst)-i-1):
      if lst[j] > lst[j+1]:
        lst[j],lst[j+1] = lst[j+1],lst[j]

if __name__ == '__main__':
  lst = [2,5,1,4,3]

  bubble_sort(lst)

  print("Sorted list is: ",lst)