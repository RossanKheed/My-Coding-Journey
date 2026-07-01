
velocity = float(input ("What is th velocity :"))
acceleration = float (input("What is acceleration :"))
time = float(input (" What is the time in seconds :"))
s = (velocity * time ) + (0.5 * acceleration) * time**2
print(f"The displacement is {s}m")