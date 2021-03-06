"""
file: quickSort.py
version: python3
author: Arthur Nunes-Harwitt, Ivona Bezakova
purpose: Implementation of the quick-sort algorithm ( not in-place )
"""

def quickSort( L ):
    """
    quickSort: List( A ) -> List( A )
        where A is 'totally ordered'
    """
    if L == []:
        return []
    else:
        pivot = L[0].value
        ( more, same, less ) = partition( pivot, L )
        return quickSort( more ) + same + quickSort( less )

def partition( pivot, L ):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    """
    ( more, same, less ) = ( [], [], [] )
    for e in L:
        if e.value < pivot:
            less.append( e )
        elif e.value > pivot:
            more.append( e )
        else:
            same.append( e )
    return ( more, same, less )

if __name__ == "__main__":
    print( quickSort( [1, 5, 3, 4, 2, 2, 7, 5, 3, 4, 9, 0, 1, 2, 5, 4, 76, 6] ) )

