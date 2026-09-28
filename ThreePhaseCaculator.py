import math

voltage = float(input("Enter  line voltage (V): "))
current = float(input("Enter line current (A): "))
power_factor = float(input("enter power factor (0-1): "))

if 0 <= power_factor <= 1: 
  power = math.sqrt(3) * voltage * current *  power_factor
  print(f"Three-phase active power = {power:.2f} W")
  print("P= sqrt(3)​×VL​×IL​×cosϕ")
 
 
else:  
  print("Invalid power factor")
  
