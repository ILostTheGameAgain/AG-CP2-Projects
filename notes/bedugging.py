#Alec George bedugging notes


import trace
import sys

def trace_calls(frame, event, arg): #three args: frame = current run (now), event = type of thing happening, arg = information being used
    if event == "call": #when function is called
        print(f"calling function: {frame.f_code.co_name}") #f code is the file, co name is the name of the function

    elif event == "line": #when a new line of code happens
        print(f"Executing line {frame.f_lineno} in {frame.f_code.co_name}") #f lineno is the linenumber

    elif event == "return": #when we return stuff
        print(f"{frame.f_code.co_name} returned {arg}")

    elif event == "exception": #when there are issues (exception)
        print(f"Exception in {frame.f_code.co_name}: {arg}")



    return trace_calls


sys.settrace(trace_calls)
tracer = trace.Trace(count=False, trace=True)

#----------------------------------------
#What is tracing?
def sub(num1, num2):
    return num1 - num2


def add(num1, num2):
    print(sub(num1, num2))
    return num1 + num2

print(add(5,4))


#tracer.run('add(3,5)')

#It allows you to access information about functions in your program
#basic tracing command
    #python -m trace --trace notes\bedugging.py

"""
    --trace (displays lines as executed)
    --count (displays number of times executed)
    --listfuncs (displays functions used in the program)
    --trackcalls (displays relationships between functions)
"""

#----------------------------------------
#What are some ways we can debug by tracing?

    #we can use this to find where errors are occuring that don't disrupt the program
    #observe what your program is doing without interrupting it

#----------------------------------------
#How do you access the debugger in VS Code?

    #click the debug button on the left
    #click f5
    #click the debug dropdown

#----------------------------------------
#What is testing?

    #running your code to make sure it works as required
    #try to break it
    #run it more than once

#----------------------------------------
#What are boundary conditions?

    #checking the edge possibilities to see that they work correctly
    #check the entries most likely to be wrong

#----------------------------------------
#How do you handle when users give strange inputs?

    #conditionals, loops, etc.