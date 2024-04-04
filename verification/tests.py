"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
        "input": [[5, 4, 3, 2, 1]],
        "answer": [[4, 5, 3, 2, 1], [3, 4, 5, 2, 1], [2, 3, 4, 5, 1], [1, 2, 3, 4, 5]]
    },
    {
        "input": [[2, 3, 1, 5, 4]],
        "answer": [[2, 3, 1, 5, 4], [1, 2, 3, 5, 4], [1, 2, 3, 5, 4], [1, 2, 3, 4, 5]]
    },
    {
        "input": [[6, 5, 4, 3, 2, 1]],
        "answer": [[5, 6, 4, 3, 2, 1], [4, 5, 6, 3, 2, 1], [3, 4, 5, 6, 2, 1], [2, 3, 4, 5, 6, 1], [1, 2, 3, 4, 5, 6]]
    }
    ]
}
