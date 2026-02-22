"""
Given an image represented by an N x N matrix, where each pixel in the image is represented by han integer,
Write a method to rotate the image by 90 degrees. Can you do this in place?
"""

# when we rotate a matrix we essentially change all the rows to columns
def rotate_matrix(matrix):
    new_matrix = []
    for column in zip(*matrix):
        print(list(column))
        new_matrix.insert(0, list(column))
    print(new_matrix)


rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
