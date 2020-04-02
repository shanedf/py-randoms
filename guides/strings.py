"""
Strings in Python - quick developers guide

String objects are immutable - string manipulation is achieved
    by creating a new object with the result and moving the 
    reference, allowing the old object to be gc'd if nothing
    else references it.

"""

def join():
    """Joins a series of objects together.

        join() should be called on the separator:

            eg: ''.join(['break','fast']) = 'breakfast'
            
            ******************************************
            *** This method should always be used  ***
            ***  rather than + style concatenation ***
            ******************************************

    Args:
        One collection item (list, tuple, etc)
    """
