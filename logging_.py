import logging
def multiplying(x:float, y:float):
    """
    param x: input variable of type float
    param y: input variable of type float
    return: returning multiplication of the 
    input variables
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        logging.error('Input variables are not of type float or integer!.')