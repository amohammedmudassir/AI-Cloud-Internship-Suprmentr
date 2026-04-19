#Assignment 6 (20/02/2026) Assignment Name : NumPy Speed Test Description : Compare Python lists vs NumPy arrays with 1M numbers, measure execution time, write 3 observations.
import numpy as np
import time
list1=[]
for i in range(1,1000001):
    list1.append(i)
array1=np.array(list1)
# Measure time for list
start_time_list=time.time()
squarred_list=[x**2 for x in list1]
end_time_list=time.time()
# Measure time for NumPy array
start_time_array=time.time()
squarred_array=array1**2
end_time_array=time.time()
# Calculate execution times
execution_time_list=end_time_list-start_time_list
execution_time_array=end_time_array-start_time_array
print(f"Execution time for Python list: {execution_time_list:.4f} seconds")
print(f"Execution time for NumPy array: {execution_time_array:.4f} seconds")

# Observations:
# 1. NumPy arrays are significantly faster than Python lists for numerical operations due to optimized C.
# 2. The execution time for squaring 1 million numbers is much lower with NumPy arrays compared to Python lists, demonstrating the efficiency of vectorized operations.
# 3. For large datasets, using NumPy can lead to substantial performance improvements, making it the preferred choice for data manipulation and scientific computing tasks.
