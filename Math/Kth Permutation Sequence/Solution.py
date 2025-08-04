def getPermutation(n: int, k: int) -> str:
    # Step 1: Manual factorial function to avoid importing math module
    def factorial(x):
        res = 1
        for i in range(2, x + 1):
            res *= i
        return res

    # Step 2: Create a list of numbers from 1 to n
    nums = [str(i) for i in range(1, n + 1)]  # ['1', '2', '3', '4'] if n = 4

    result = []  # to store the final permutation

    # Step 3: We don't convert k to 0-based index globally
    # Instead, we handle 1-based indexing by adjusting (k - 1) inside the loop

    for i in range(n, 0, -1):
        # Total permutations for the remaining (i-1) digits
        f = factorial(i - 1)

        # Find the index of the digit to place at the current position
        index = (k - 1) // f

        # Add the selected digit to result
        result.append(nums.pop(index))

        # Update k to find the next digit in the remaining list
        k -= index * f

        # Example Dry Run:
        # For n=4, k=9
        # Iteration 1: f=6, index=(9-1)//6=1 => pick '2', nums=['1','3','4'], k=9-6=3
        # Iteration 2: f=2, index=(3-1)//2=1 => pick '3', nums=['1','4'], k=3-2=1
        # Iteration 3: f=1, index=(1-1)//1=0 => pick '1', nums=['4'], k=1
        # Iteration 4: f=1, index=(1-1)//1=0 => pick '4', nums=[]
        # Result: '2314'

    return ''.join(result)

# Test the function with an example
if __name__ == "__main__":
    print(getPermutation(4, 9))  # Output should be "2314"
