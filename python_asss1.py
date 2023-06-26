'''Q1'''
def get_odd_numbers():
    odd_numbers = []
    for num in range(1, 26):
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers

# Call the function
result = get_odd_numbers()
print(result)

'''Q2'''
'''The *args syntax allows a function to accept any number of positional arguments. It allows you to pass a 
variable-length list of arguments to the function. Within the function, args is treated as a tuple that contains 
all the positional arguments passed.
Here's an example function that demonstrates the use of *args:'''
def greet(*args):
    for name in args:
        print("Hello,", name)

# Call the function
greet("Alice", "Bob", "Charlie")
'''Now let's move on to **kwargs. This syntax allows a function to accept any number of keyword arguments 
(i.e., arguments specified with a name). It allows you to pass a variable-length dictionary of key-value pairs 
to the function. Within the function, kwargs is treated as a dictionary that contains all the keyword arguments 
passed.
Here's an example function that demonstrates the use of **kwargs:'''
def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(key + ":", value)

# Call the function
describe_person(name="Alice", age=25, country="USA")

'''Q3'''
'''In Python, an iterator is an object that allows sequential access to elements in a container or collection. 
It provides a way to loop over a sequence of values without the need to know the specific implementation details 
of the underlying data structure.
To create an iterator in Python, you need to implement two methods: __iter__() and __next__().
The __iter__() method is used to initialize the iterator object. It returns the iterator object itself and is 
responsible for setting up any necessary state for iteration.
The __next__() method is used to retrieve the next element in the iteration sequence. It returns the next value in 
the sequence and advances the iterator. If there are no more elements, it raises the StopIteration exception to 
signal the end of iteration.'''
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

class NumberIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

# Create an iterator object
iterator = NumberIterator(numbers)

# Iterate and print the first five elements
for _ in range(5):
    element = next(iterator)
    print(element)

'''Q4'''
'''In Python, a generator function is a special type of function that generates a sequence of values 
on-the-fly, as opposed to returning them all at once like a regular function. It uses the yield keyword to 
produce a series of values, one at a time, whenever the generator is iterated over.
The main advantage of using a generator function is that it allows you to generate and process large sequences
of values efficiently, without needing to store them all in memory simultaneously. This can be particularly 
useful when dealing with infinite sequences or when working with large datasets.
The yield keyword is used in a generator function to define points at which the function's execution will be 
suspended, and the yielded value will be returned to the caller. The function's state is preserved, allowing it 
to resume execution from where it left off when the next value is requested.'''
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the generator function
fib_gen = fibonacci()

# Iterating over the generated sequence
for i in range(10):
    print(next(fib_gen))

'''Q5'''
def prime_generator():
    primes = []
    num = 2

    while num < 1000:
        is_prime = True

        for prime in primes:
            if prime * prime > num:
                break
            if num % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)
            yield num

        num += 1

# Using the generator function
prime_gen = prime_generator()

# Printing the first 20 prime numbers
for _ in range(20):
    print(next(prime_gen))

'''Q6'''
# Initializing variables
a, b = 0, 1
count = 0

# Printing the first 10 Fibonacci numbers
while count < 10:
    print(a)
    a, b = b, a + b
    count += 1

'''Q7'''
string = 'pwskills'
output = [char for char in string if char in 'pwskills']
print(output)

'''Q8'''
number = int(input("Enter a number: "))
temp = number
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = (reverse * 10) + digit
    temp //= 10

if number == reverse:
    print(number, "is a palindrome.")
else:
    print(number, "is not a palindrome.")

'''Q9'''
odd_numbers = [num for num in range(1, 101) if num % 2 != 0]
print(odd_numbers)
