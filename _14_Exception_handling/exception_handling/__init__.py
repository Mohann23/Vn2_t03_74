'''
syntax errors
logical errors --- Exceptions

Try  --- lines of code
Except
Else
Finallly



'''








try:
    def fun(a):
        if a < 4:  # throws ZeroDivisionError for a = 3
            b = a / (a - 3)  # throws NameError if a >= 4
        print("Value of b = ", b)
    fun(1)
    print("--------------------")
    fun(3)
    print("+++++++++++++++++++++")
    fun(10)



# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError :
    print("NameError Occurred and Handled")

