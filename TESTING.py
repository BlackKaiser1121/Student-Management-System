import random
def quick_sort_random(arr): 
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr) 
    print(f"Pivot: {pivot}")  
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_random(left) + middle + quick_sort_random(right)


arr = [10, 7, 8, 9, 1, 5]
print("Original:", arr)
print("Sorted:", quick_sort_random(arr))
