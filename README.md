# Final Exam Shifting Left

Final Exam - A program to cyclically shift the elements of an array to the left by $n$ positions.

## 📝 Description

Write a function, `cyclic_left_shift(array, n)`, that takes an array and an integer $n$ and returns a new array with its elements shifted to the left by $n$ positions. The shift should wrap around, meaning elements that move past the beginning of the array appear at the end.

-----

## 🎯 Problem Statement

### Input:

  * Input 1: An array (list) of integers.
  * Input 2: An integer $n$ (the number of positions to shift).

### Output:

  * The new array (list) with elements shifted.
  * "No proceed" if the input is not a list or is an empty list.

### Rules:

1.  The elements of the array must be shifted to the left by $n$ positions.
2.  The shift is cyclic (wraps around).
3.  If $n$ is larger than the array length, the shift should still wrap correctly (e.g., $n = 7$ on a 3-element array is the same as $n = 1$).
4.  If the input is not a list or is an empty list, return "No proceed".

-----

## 💡 Examples

### Example 1 (Sample 1)

**Input:**

```
[1, 2, 3, 4, 5]
2
```

**Output:**

```
[3, 4, 5, 1, 2]
```

**Explanation:** The array is shifted left by 2, and `[1, 2]` wraps to the end.

### Example 2 (Sample 4)

**Input:**

```
[0, 9, 8, 7, 6]
3
```

**Output:**

```
[7, 6, 0, 9, 8]
```

**Explanation:** The array is shifted left by 3, and `[0, 9, 8]` wraps to the end.

### Example 3 (Sample 5)

**Input:**

```
[100, 200,  300]
7
```

**Output:**

```
[200, 300, 100]
```

**Explanation:** A shift of 7 is equivalent to $7 \pmod 3 = 1$. A shift of 1 moves `[100]` to the end.

### Example 4 (Sample 6)

**Input:**

```
[]
```

**Output:**

```
No proceed
```

**Explanation:** The input array is empty.

-----

## 🚀 How to Use

1.  **Clone this repository**

    ```bash
    git clone https://github.com/adiaryaz/shifting-left.git
    cd shifting-left
    ```

2.  **Run the program** (assuming the file is `Shifting Left_UAS-M4.py`):

    ```bash
    python "Shifting Left_UAS-M4.py"
    ```

    Enter the array (e.g., `[1, 2, 3]`) and shift value on separate lines.

-----
