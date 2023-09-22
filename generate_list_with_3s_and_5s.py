"""
Here we need to generate a list which contains  either 3s' or 5s'  existed in the given range.
If the range is between 1-50 then list should be like below.
l=[3,5,13,15,23,25,30,31,32.....43,45,50]
here 50 is included
"""

l = [ele for ele in range(1, 51) if '3' in str(ele) or '5' in str(ele)]
print(l)
