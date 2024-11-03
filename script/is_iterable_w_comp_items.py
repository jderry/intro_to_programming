def is_iterable_w_comp_items(arry: list|tuple) -> bool:
    ''' Given a collection of items,
        returns a bool:
        True if collection is iterable
        AND all its items are comparable;
        otherwise, False
    '''
    try:
        iter(arry)

    except TypeError:
        return False
    
    for index, value in enumerate(arry):
        try:
            if index < len(arry):
                arry[index] > arry[index+1]
            return True
        except TypeError:
            return False
