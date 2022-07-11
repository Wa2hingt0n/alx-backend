#!/usr/bin/env python3
""" Defines a function 'index _range' """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        patricular pagination parameters

    Args:
        page: The page to be returned
        page-size: The size of one page
    """
    first_idx = (page - 1) * page_size
    last_idx = first_idx + page_size
    return (first_idx, last_idx)
