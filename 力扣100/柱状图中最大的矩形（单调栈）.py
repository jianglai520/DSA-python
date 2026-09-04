from typing import List

def largestRectangleArea(heights: List[int]) -> int:
    heights.append(0)

    stack = []
    max_area = 0

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            left = stack[-1] if stack else -1
            width = i - left - 1
            area = width * height
            max_area = max(max_area, area)
        stack.append(i)
    return max_area