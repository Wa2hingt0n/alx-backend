#!/usr/bin/env python3
""" Defines a pagination helper function 'index_range' and class 'Server' """
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters
    Args:
        page: The page to be returned
        page-size: The size of one page
    """
    first_idx = (page - 1) * page_size
    last_idx = first_idx + page_size
    return (first_idx, last_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ Class constructor """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Returns the appropriate page from a dataset """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        indexes = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[indexes[0]: indexes[1]]
