import math

print("PART ONE: VARIABLES AND ASSIGNMENTS\n")
name = "Caleb Brown"
age = 19
height = 5.83
favorite_color = "Green"

print(name)
print(age)
print(height)
print(favorite_color)

print()

print(name,age,height,favorite_color)

print()

print(f"Name: {name}\nAge: {age}\nHeight{height}\nFavorite Color: {favorite_color}")

print()

print(f"""
Name: {name}
Age: {age}
Height{height}
Favorite Color: {favorite_color}""")

print()

circle_area = math.pi * 5**2

print()

print(f"Circle's area: {circle_area:.1f}")

print("\nPART TWO: STATEMENTS AND MODULES\n")

print(f"Square root of Age: {math.sqrt(age)}")
print(f"Sine of height: {math.sin(height)}\nCosine of height: {math.cos(height)}")

print("\nPART THREE: EXPRESSIONS AND OPERATORS\n")

print(f"""Age + 5: {age+5}
Difference between height and 4(absolute value): {math.fabs(height-4)}
product of age and height: {age+height}
quotient of height and 2: {height/2}
The remainder of age divided by 3: {age%3}
age raised to the power of 2: {age**2}""")

	print("\nPART FOUR: TEMPERATURE CONVERSION:\n")

#Converting temperatures
temp = "NaN"
while type(temp) == str:
	temp = input("Please enter a tmperature in Fahrenheit: ")
	try:
		temp = float(temp)
	except Exception:
		print("Please enter a number")
celsius = (temp - 32) * 5/9
if temp == 451:
	print("It was a pleasure to burn. It was a special pleasure to see things eaten, to see things blackened and changed.\n")
print(f"Temperature in celsius: {celsius}\N{DEGREE SIGN}")