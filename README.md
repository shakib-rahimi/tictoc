## Usage

The easiest way to calculate the execution time of any part of the program in Python
sample code:

"""

    from tictoc import tic, toc
    
    tic()
    
    <some codes>

    toc()       # to show the execution time directly with built-in print function
    
    #-----------------------------------------#
    
    tic()
    
    <some codes 2>
    
    execution_time = toc(False) # do not show, but return as a variable
    
"""
