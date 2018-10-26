"""
Name: Area.py
Purpose: Calculates the area of a triangle or circle
Name: Trevor
Date: 10/26/18
"""

print('The calculator has started.')
option = input('Enter C for Circle and T for Triangle: ')
                   
if option == 'C':
    
    radius = float(input('Enter the radius: '))
    area = 3.14159 * radius ** 2
    print(str(area))

elif option == 'T':
    base = float(input('Enter the base: '))
    height = float(input('Enter the height: '))
    area = 0.5 * base * height
    print(str(area))
  
print('Exiting...')
