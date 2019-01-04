types_of_people = 10
x = f"There are {types_of_people} types of people."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
# Inserts hilarious variable into the empty braces of joke_evaluation
print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."
# Concats w and e to print one string
print(w + e)


