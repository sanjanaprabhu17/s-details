import sys

if len(sys.argv) == 3:
    script_name = sys.argv[0]
    name = sys.argv[1]
    rollno = sys.argv[2]
    print("User provided input values:")
else:
    script_name = sys.argv[0]
    name = "misbah"
    rollno = "058"
    print("No input given, using default values:")

print("Script name:", script_name)
print("Student name:", name)
print("Roll number:", rollno)
