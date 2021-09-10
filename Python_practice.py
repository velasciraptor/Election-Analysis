print("Hello World!")

# What is the score?
score = int(input("What is your test score? "))

# 3.2.8 Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

# 3.2.9 Membership & Logical Operators
   
    # Membership Operators: in & not in
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
   print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

    # Logical Operators: and, or, not
    # and = if both are True, or = if either is True, not = expression is True if conditional is False
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
  
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

# 3.2.10 Repetition Statements
    # While loops
x = 0
while x <= 5:
    print(x)
    x = x + 1

    #For loops
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
    #You can use range instead to simplify code
for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

    # For loops in dictionariers
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county, voters in counties_dict.items():
    print(county, voters)

# 3.2.11 F-Strings & Printing formats

    # Using Concatentaion
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.") 

    # Using F-String
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")   

    # Multi-line F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate) 

    # Format a long decimal with f'{value:{width}.{precision}}
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# 3.4.1 Python Dependencies, Modules, and Packages; Russian nesting dolls

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)