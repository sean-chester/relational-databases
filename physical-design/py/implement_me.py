# Implementation of B+-tree functionality.

from index import *
from log import *

# You should implement all of the static functions declared
# in the ImplementMe class and submit this (and only this!) file.
class ImplementMe:

    # Returns a B+-tree obtained by replaying the REDO log file.
    # Unseen values should be inserted;
    # previously seen values should be deleted and re-inserted.
    # Values that were never committed should never be inserted.
    # @precondition: the log file will not try to add an existing key
    #
    # Complexity: Each operation is guaranteed to be asymptotically
    # linear in the height, h, of the tree, O(h).
    # Because the tree is balanced, it is also asymptotically logarithmic in the
    # number of keys, n, that already exist in the index, i.e., O(h) = O(lg n).
    # The entire insertion of a log of length L should be O(L lg n)
    @staticmethod
    def from_log( log ):
        return Index()

    # Returns a list of keys visited by a lookup query to ascertain
    # whether a given key is found among the leaves of a B+-tree index.
    #
    # Complexity: Guaranteed not to touch more nodes than the
    # height of the tree
    @staticmethod
    def lookup( index, key ):
        return []

    # Returns a list of keys visited by a range query in a B+-tree index
    # within the closed interval [lower_bound, upper_bound]
    #
    # Complexity: Guaranteed not to touch more nodes than the height
    # of the tree and the number of leaves overlapping the interval.
    @staticmethod
    def range( index, lower_bound, upper_bound ):
        return []
