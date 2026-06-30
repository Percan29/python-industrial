points = [0.2, 0.4, 0.6, 0.8]

def weld_sequence(points):
    for pos in points:
        print(f"Moving to position {pos}")
        print("Welding with speed=18 and length=12")

weld_sequence(points)

# Note:
# This script simulates an industrial welding sequence,
# showing basic operating parameters and positions.
# It is a demonstration of applied logic for technical processes
# in automated environments with cobots.
