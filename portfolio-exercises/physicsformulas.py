import math

def calculate_physics():
    print("Welcome to the Physics Engine!")
    print("1: Kinetic Energy (K.E)")
    print("2: Orbital Velocity (Vo)")
    
    choice = input("Choose a formula (1 or 2): ")
    
    if choice == '1':
        m = float(input("Enter mass (m): "))
        v = float(input("Enter velocity (v): "))
        result = 0.5 * m * v**2
        print(f"The K.E is: {result} Joules")
        
    elif choice == '2':
        G = 6.674e-11 # Universal Gravitational Constant
        M = float(input("Enter mass of planet (M): "))
        r = float(input("Enter radius (r): "))
        result = math.sqrt((G * M) / r)
        print(f"The Orbital Velocity is: {result} m/s")
    
    else:
        print("Invalid choice, keep leveling up!")

# Run the game
calculate_physics()
