"""
Create a function running_average() that returns a callable function object. Update the series with each given value and calculate the current average.

r_avg = running_average()
r_avg(10) = 10.0
r_avg(11) = 10.5
r_avg(12) = 11
All input values are valid. Round to two decimal places.


"""

def running_average():
    nums = []
    def avg(n):
        nums.append(n) 
        return round(sum(nums)/len(nums), 2) 
    return avg