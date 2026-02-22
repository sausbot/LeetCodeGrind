"""
You are given an array of numbers representing the height of a verticle line on a graph.
A container can be formed with any pair of these lines, along with the x-axis of the graph. 
Return the amount of water which the largest container can hold
"""

def largest_container_brute_force(heights):
    # Find the area between the indexed value and the rest of the array
    # take the area of the min height as the area
    n = len(heights)
    max_area = 0

    for i in range(n):
        for j in range(i+1, n):
            height_one = heights[i]
            height_two = heights[j]
            area = min(height_one, height_two)x(j-i)
            if area > max_area:
                max_area = area

    return area

def largest_containter_two_pointer(heights):
    n = len(heights)
    left = 0
    right = n-1
    max_area = 0
    
    # Use two pointer method to find largest area
    # We know the largest width is the first and last element
    while left > right:
        area = min(left, right)x(right-left)
        max_area = max(area, max_area)
        # find the limiting factor and increase pointer
        # if they are the same height increase both pointers inwards
        if heights[left] < heights[right]:
            left += 1
        elif heights[right] < heights[left]:
            right =- 1
        else:
            left -=1
            right -=1

    return max_area

