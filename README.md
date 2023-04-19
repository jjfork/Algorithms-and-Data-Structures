# Sorting algorithms in Python

A brief description of what this project does

# SortingAlgorithmsPython

This is a Python project that implements several sorting algorithms, including:

Usage
main.py is the entry point for the project. It contains a function get_mean_time_for_algorithms that calculates the mean
time for each sorting algorithm for a given array size.

To run the project, simply execute main.py.

```bash
python main.py
```

To run heap_sort

```bash
python binaryTress/heap_sort.py
```

To run BST

```bash
python binaryTress/BST.py
```

numpy
matplotlib
You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

## Simple algorithms

bubble_sort.py contains the implementation of the Bubble Sort algorithm. The bubble_sort function takes an input array
and sorts it in ascending order.

insertion_sort.py contains the implementation of the Insertion Sort algorithm. The insertion_sort function takes an
input array and sorts it in ascending order.

radix_sort.py contains the implementation of the Radix Sort algorithm. The radix_sort function takes an input array and
sorts it in ascending order.

selection_sort.py contains the implementation of the Selection Sort algorithm. The selection_sort function takes an
input array and sorts it in ascending order.

## Conclusions simple algorithms

To determine what type of mathematical function is represented by these results, we can look at the increase in
execution time of the algorithms as the size of the sorted array increases.

We can see that for each algorithm, the execution time increases as the size of the array increases. However, the rate
of increase in execution time varies from algorithm to algorithm.

For selection_sort and bubble_sort, the execution time increases exponentially (exponentially). This can be seen from
the fact that the execution time grows very rapidly as the array size increases, and applying these algorithms to very
large arrays can cause the execution time to become unacceptably long.

For insertion_sort, the execution time increases quadratically (polynomially). This can be seen from the fact that the
rate of increase in execution time is slower than for selection_sort and bubble_sort, but it is still quite fast and can
become problematic for large array sizes.

Therefore, from these results, it can be deduced that the mathematical function presented is primarily an exponential (
exponential) function, and for insertion_sort also a polynomial (quadratic) function.

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

## Binary Tree

1) heap and heap sort:
   Analyzing the graph, it can be seen that the time complexity of heapsort sorting is of the order of O(n log n).
   The curves in the graph are very close to logarithmic functions, which confirms the theoretical complexity of
   sorting.
   ![Chart](https://user-images.githubusercontent.com/91293626/233057453-fa98bbff-ce66-4fa0-a140-f0228e644ab1.png)
2) BST:
   We see that the curve in the graph grows nonlinearly with the length of the vector, suggesting a binary search tree
   search time complexity of O(log n). This is the expected result, since BST is well known for its use in fast search
   algorithms, in which the search time is proportional to the height of the tree.
    ![Chart](https://user-images.githubusercontent.com/91293626/233059430-9da9b71d-5b0d-4a7c-abe6-7c0f24f873e8.png)
It can also be noted that for shorter vectors (lengths of 100 and 500) the curve is more "rough" and more like a
logarithmic function, while for longer vectors (lengths of 1000 and 2000) the curve is smoother and more like a
quadratic function. This is because for shorter vectors the span of values in the tree is smaller and the tree is less
balanced, which can affect the search time. For longer vectors, the tree becomes more balanced and the search time can
depend on the number of nodes in the tree.

## Authors

- [Jakubiak, Julian](https://github.com/jjfork)
