
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:

# print(x)

# check Exception
try:
    print(x)
except Exception as e:
    print(e)

# write custom meesage on Exception
try:
    print(x)
except NameError:
    print("Variable is not defined first define it ")



# Mulitple Except blocks
try:
    print(2/0)
except NameError:
    print("Variable is not defined first define it ")
except:
    print("Something went wrong")



# else block
try:
    print(2)
except NameError:
    print("Variable is not defined first define it ")
except:
    print("Something went wrong")
else:
    print("Everything is fine")



# fanally block
try:
    print(x)
except:
    print("Variable is not defined first define it ")
finally:
    print("The try except block executed succefully")

