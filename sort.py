def partition(start, end, array):         
    pivot_index = start 
    pivot = array[pivot_index][0]          
    while start < end:        
        while start < len(array) and array[start][0] <= pivot:
            start += 1        
        while array[end][0] > pivot:
            end -= 1               
        if(start < end):
            array[start], array[end] = array[end], array[start]         
    array[end], array[pivot_index] = array[pivot_index], array[end]         
    return end
      
# The main function that implements QuickSort 
def quick_sort(start, end, array):      
    if (start < end):        
        p = partition(start, end, array)       
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)
          

# gg = [ 10, 7, 8, 9, 1, 5 ]
# aa =    ['f','c','d','e','a','b']
# array = list(zip(gg,aa))
# print(array[0]<array[1])
# quick_sort(0, len(array) - 1, array)  
# print(f'Sorted array: {array}')
      