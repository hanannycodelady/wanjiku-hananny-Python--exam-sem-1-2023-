#(i) calculating the area of the circle
def calculate_area(radius):
    area = 3.14 * (radius ** 2)
    return area

radius = 5
area = calculate_area(radius)
print("Area of the circle:", area)

#(ii) sum of natural numbers
def calculate_sum(n):
    if n == 0:
        return 0
    else:
        return n + calculate_sum(n-1)
    n = 4
sum = calculate_sum(4)
print("Sum of natural numbers up to", 4, ":", sum)

#(iii) removing element at index 2 and inserting value 10 at the end
numbers = [1, 3, 5, 7, 9]
del numbers[2]
numbers.append(10)
print("Updated numbers list:", numbers)


#(iv) 
original_list = [2, 4, 6, 8, 10]
even_numbers = [num for num in original_list if num % 2 == 0]
print("New list with even numbers:", even_numbers)

#(v)


#(vi) 
original_dict = {'a': 3, 'b': 8, 'c': 2, 'd': 7}
new_dict = {key: value for key, value in original_dict.items() if value > 5}
print("New dictionary with values greater than 5:", new_dict)




