def my_function():
  print("Hello from a function")

#------------------------
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#----------------------------

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#-------------------------

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#--------
def my_function(x):
  return 5 * x

print(my_function(3))

#-------------------
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Rekürsif")
tri_recursion(6)

#--------------------
