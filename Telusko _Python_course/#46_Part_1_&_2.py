#_main_  is the starting point of the python. 
#The first module name is always main and the code starts from main.
#_name_ is a variable name that return the __main__.
#name_ is a built in variable that evaluates the name of the current module.
#The value of the name changes as per the place where it is used, so that's why it is known as a variable.
#If you are an individual file or module, then the name will return main. 
#If you are importing another module containing the name variable in any file, then the name variable will return the name of that module.

#If you are running a file as a main and using a named variable in it, then it will print the main.
#But if you are printing a name that is imported as a module in another file, then it will print the module name.


#The use of a function with the name variable helps the interpreter in checking if it's parsing the currently executed script, or if it's temporarily parsing another external script. 
#if _name_ == "__main__":
#This statement helps us to control the behaviour of different parts of the program.
#It chooses the number of lines of codes that can be executed from the external script as well as the currently executed script depending on the scenarios.