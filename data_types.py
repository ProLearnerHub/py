def data_types():
  'string', # a string is data that represents a combination of alphanumeric characters. Is usually written using quotation marks (both single and double are okay, but they're usually written using double quotation marks)
  0, # an integer is data that represents a whole number
  1.2, # an float is data that represents a floating point number (with decimals)
  True, # a boolean is data that represents truthy or falsy values. Can only either be true or false
  {}, # a dictionary is data that represents keyed collections, that is, 'key' & 'value' pairs, disallowing duplicates
  [], # a list is a collection of different, ordered data. Can contain data of any type. (eg, a class is an array of students and teachers and books and pens)
  def function():
    return 'a function processes input to produce an output'
            # in python, functions are declared using the 'def' keyword, followed by the name of the function, followed by open and closed braces, inside of which we may add any parameters, then a single colon mark.
            
def about_functions():
  return
  # in python, functions are not written using curly braces for the function body. Instead, it uses indentation (a single tab, equivalent to 4 whitespaces)
  # everything that falls in the same indentation is considered part of the function body
  # to pass parameters, we will write as below
  
def function_params(parameter_one, parameter_two):
  # process parameters however, eg adding two numbers
  return parameter_one + parameter_two
  
  # above, we have a function that takes two parameters and returns a value based on computations set for the parameters, in this case, a number and another number
  # a function can return any data type, so long as the 'return' keyword is included.
  # generally, in most programming languages, the 'return' keyword ends a function call, meaning nothing that folloows after will be executed, and it will terminate
  # if no return value is included, a function will return 'None', which means nothing that exists, it is unknown, it is not in memory.
  # to exit a function, just jump out of the indentation, as below
  
  
# to call a function, we use the name we gave the function, and if any parameters, we pass them as well, eg

about_functions()

# or

function_params(1, 5) # returns 6, after adding the values passed to it
  
