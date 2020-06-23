name = "Bob"
greeting = "Hello, Bob"

print(greeting)

name = "Rolf"

print(greeting)

greeting = f"Hello, {name}"
print(greeting)

# --

name = "Anne"
print(
    greeting
)  

print(
    f"Hello, {name}"
)  

# -- Using .format() --

greeting = "Hello, {}"
with_name = greeting.format("Rolf")
print(with_name)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)