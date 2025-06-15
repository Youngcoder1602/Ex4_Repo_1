import matplotlib.pyplot as plt

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        l = r = i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                arr[i] = left[l]
                l += 1
            else:
                arr[i] = right[r]
                r += 1
            i += 1

        while l < len(left):
            arr[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            arr[i] = right[r]
            r += 1
            i += 1


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list, label = 'Before sorting')
plt.show()

mergeSort(my_list)

x = range(len(my_list))
plt.plot(x, my_list, label = 'After sorting')
plt.show()
