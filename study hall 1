from collections import Counter
import math

#mean

n_num = [1, 2, 3, 4, 5]
n = len(n_num)
  
get_sum = sum(n_num)
mean = get_sum / n
  
print("Mean is: " + str(mean))

#median
n_num = [1, 2, 3, 4, 5]
n = len(n_num)
n_num.sort()
  
if n % 2 == 0:
    median1 = n_num[n//2]
    median2 = n_num[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = n_num[n//2]
print("Median is: " + str(median))

#mode
n_num = [1, 2, 3, 4, 5, 5]
n = len(n_num)
  
data = Counter(n_num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
  
if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is: " + ', '.join(map(str, mode))
      
print(get_mode)

#sd
xs = [0.2,0.3,0.5,0.9]    
mean = sum(xs) / len(xs)   
var  = sum(pow(x-mean,2) for x in xs) / len(xs)  
std  = math.sqrt(var)

print("standard deviation is: ",std)
