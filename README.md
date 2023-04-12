
# Sorting algorithms in Python

A brief description of what this project does

# SortingAlgorithmsPython

This is a Python project that implements several sorting algorithms, including:


Usage
main.py is the entry point for the project. It contains a function get_mean_time_for_algorithms that calculates the mean time for each sorting algorithm for a given array size.

To run the project, simply execute main.py.

```bash
python main.py
```

numpy
matplotlib
You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

## Simple algorithms

bubble_sort.py contains the implementation of the Bubble Sort algorithm. The bubble_sort function takes an input array and sorts it in ascending order.

insertion_sort.py contains the implementation of the Insertion Sort algorithm. The insertion_sort function takes an input array and sorts it in ascending order.

radix_sort.py contains the implementation of the Radix Sort algorithm. The radix_sort function takes an input array and sorts it in ascending order.

selection_sort.py contains the implementation of the Selection Sort algorithm. The selection_sort function takes an input array and sorts it in ascending order.

## Conclusions simple algorithms

To determine what type of mathematical function is represented by these results, we can look at the increase in execution time of the algorithms as the size of the sorted array increases.

We can see that for each algorithm, the execution time increases as the size of the array increases. However, the rate of increase in execution time varies from algorithm to algorithm.

For selection_sort and bubble_sort, the execution time increases exponentially (exponentially). This can be seen from the fact that the execution time grows very rapidly as the array size increases, and applying these algorithms to very large arrays can cause the execution time to become unacceptably long.

For insertion_sort, the execution time increases quadratically (polynomially). This can be seen from the fact that the rate of increase in execution time is slower than for selection_sort and bubble_sort, but it is still quite fast and can become problematic for large array sizes.

Therefore, from these results, it can be deduced that the mathematical function presented is primarily an exponential (exponential) function, and for insertion_sort also a polynomial (quadratic) function.

![Chart](https://user-images.githubusercontent.com/91293626/226912331-2abc1097-5293-4b44-b2bd-55e1e3196f7a.png)



## advanced algorithms
Counting_sort

Merge_sort

Quick_sort


## Conclusions advanced algorithms

in this statement on the charts will be shown 
1) optimistic and pessimistic scenario and random array for quick_sort
2) optimistic and pessimistic scenario and random array for merge_sort
3) optimistic and pessimistic scenario and random array for
counting_sort
4) time of algorithms for random array

![Chart](https://user-images.githubusercontent.com/91293626/231471380-66f170a3-aa9c-40e0-80f7-71dd1497a32f.png)


## Authors

- [Jakubiak, Julian](https://github.com/jjfork)
