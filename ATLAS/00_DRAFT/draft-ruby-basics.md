---
tags:
  - learning
created: "[[2025-06-03]]"
HUB:
  - "[[hub-ruby]]"
---

![[concept-introduction-to-ruby]]

# Getting Started


- the puts method 
```ruby
3 + 5

puts 1
puts 1 + 2
puts(1 + 2)

  

puts "Hello world"
puts "I'm alive and well!"

  

puts 3.14159

puts

puts "Afterwards"

  

puts 5
puts 3
puts 5

puts 5, 3, 5
```

- Escape Characters
```ruby
puts "some text\nmore text"

puts "\tOnce upon a time"

  

puts "Juliet said \"Goodbye\" to Romeo"

puts 'Juliet said \'Goodbye\' to Romeo'

  

puts "Juliet said 'Goodbye' to Romeo"

puts 'Juliet said "Goodbye" to Romeo'
```

- The print method
```ruby
print "This random nonsense "

print "will continue on the same line"
```

- The p method
```ruby
puts "Steven Seagal"

p "Steven Seagal"

  

puts 5

puts "5"

p 5

p "5"

  

puts "Hi there\nline break"

p "Hi there\nline break"
```

- Comments
```ruby
# The code below adds 2 numbers together

# Another comment right here

# Another comment down below

puts 1 + 1

puts 2 + 2 # This will still work

puts 3 + 3
```
- Multi-line comments 
```ruby
=begin

Hello there!

This is a multi-line comment

Lots of fun code down below

Have a blast!

=end

  

puts 1 + 3
```

- integers and floating pointing numbers
```ruby
puts 100

puts 0

puts -837

puts 1_000

puts 9_999_999_999_999_999

  

puts

  

puts 3.14

puts 0.50

puts -10.99

puts -0.93
```
- basic Arithmetic in ruby 
```ruby

puts 23 % 4

  

puts 1 + 4

puts -6 + 13

puts 10 - 6

puts 3 * 4

puts 3 * 4 * 5

  

# PEMDAS

# Parentheses, Exponents, Multiplication, Division, Addition, Subtraction

puts (2 + 3) * 5

  

puts 10 / 5

puts 12 / 5

  

puts 12.0 / 5

puts 12 / 5.0

puts 12.0 / 5.0

  

puts 0.5 / 2

  

puts 5 % 2

puts 7 % 2

puts 6 % 2
```

- String concatenation
```ruby
puts 4 + 3

puts "race" + "car"

  

puts "4" + "3"
```

- Intro to Exceptions - TypeError  
```ruby
puts 3 + 4

puts "mis" + "fortune"

  

# puts "4" + 3

# puts 3 + "4"
```



# Variables


- Declaring variables
```ruby
age = 31

puts age

  

name = "Boris"

last_name = "Danger"

puts name

puts last_name

  

puts age + 7 # 31 + 7

puts name + last_name

  

age = 35

puts age

  

age_in_ten_years = age + 10 # 45

puts age_in_ten_years

  

age = age + 7 # 42

puts age

  

chameleon = 24

chameleon = "Some random text"

chameleon = 3.14

puts chameleon
```

- Exceptions - NameError 
```ruby

favorite_food = "Sushi"

  

puts favorite_food
```
- Parallel Variable Assignment
```ruby
a = 10

b = 20

c = 30

puts a, b, c

  

a, b, c = 10, 20, 30

puts a, b, c
```
- Swapping Variable Values 
```ruby
a = 1

b = 2

puts a, b

  

a, b = b, a # 2, 1

puts a, b
```
- Assignment Shortcuts
```ruby
a = 10

# a = a + 5

a += 7

puts a

  

b = 100

# b = b - 40

b -= 40

puts b

  

c = 3

# c = c * 4

c *= 4

puts c

  

name = "Boris"

name += " The Great"

puts name

```
- Constants 
```ruby
PI = 3.14159

TAX_RATE = 0.07

  

puts PI

puts TAX_RATE

  

# TAX_RATE = 0.13

# puts TAX_RATE
```




# Object methods

- intro to object methods
- Integer methods
- Exceptions : NoMethodError
- Method Chaining
- The inspect Method
- The inspect Method
- The nil Object
- String Interpolation
- The class method
- Methods to Convert Objects 





