z = 23  # Defining a variable a global scope


def variable_local():
    z = False  # defining a variable a local scope
    y = 400  # This variable is not defined
    print(z)
    print(y)


print(variable_local())

# Using a global in function
d = True


def variable_global():
    global c  # Here we have declared the variable completely inside the function
    d = 1000
    c = 200
    print(f"This variable is global: {d}")
    print(f"This variable is local and not use: {c}")


variable_global()
print(d)
print(c)


# View value with using dir


def dir_variables(a, b):
    print(a, b)
    print(dir())


print(dir_variables('First', 'Second'))
