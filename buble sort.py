array=[5,4,3,2,1]
print("Arreglo desordenado: ",array)
#O(n^2)
def bublesort(array):
    #O(n)
    for i in range(len(array)): #this amount of passes are needed to be sure the accommodation is done
        #O(n)
        for j in range(len(array)-1): #j accesses the elements of the array
            if array[j] > array[j+1]: #if the number is greater than the next they are changed
                aux=array[j] #We save the current number in a variable
                array[j]=array[j+1] #the number at the current position changes to the next number on the list
                array[j+1]=aux #the number in the next position becomes the one that was on the current position (the greater number)
    return array


print("Arreglo ordenado: ",bublesort(array))