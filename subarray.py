# Python3 program for the above approach 
import sys 

# Function to find the length of the 
# smallest subarray to be removed such 
# that sum of elements is divisible by K 
def removeSmallestSubarray(arr, n, k): 
	
	# Stores the remainder of each 
	# arr[i] when divided by K 
	mod_arr = [0] * n 

	# Stores total sum of elements 
	total_sum = 0

	# K has been added to each arr[i] 
	# to handle -ve integers 
	for i in range(n) : 
		mod_arr[i] = (arr[i] + k) % k 

		# Update the total sum 
		total_sum += arr[i] 
		
	# Remainder when total_sum 
	# is divided by K 
	target_remainder = total_sum % k 

	# If given array is already 
	# divisible by K 
	if (target_remainder == 0): 
		print("0") 
		return
	
	# Stores curr_remainder and the 
	# most recent index at which 
	# curr_remainder has occurred 
	map1 = {} 
	map1[0] = -1

	curr_remainder = 0

	# Stores required answer 
	res = sys.maxsize 

	for i in range(n): 
		
		# Add current element to 
		# curr_sum and take mod 
		curr_remainder = (curr_remainder +
							arr[i] + k) % k 

		# Update current remainder index 
		map1[curr_remainder] = i 

		mod = (curr_remainder -
			target_remainder + k) % k 

		# If mod already exists in map 
		# the subarray exists 
		if (mod in map1.keys()): 
			res = min(res, i - map1[mod]) 
	
	# If not possible 
	if (res == sys.maxsize or res == n): 
		res = -1
	
	# Print the result 
	print(res) 

# Driver Code 

# Given array arr[] 
arr = [ 3, 1, 4, 2 ] 

# Size of array 
N = len(arr) 

# Given K 
K = 6

# Function Call 
removeSmallestSubarray(arr, N, K) 

# This code is contributed by susmitakundugoaldanga
