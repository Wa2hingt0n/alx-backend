#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ Returns a dictionary with pagination parameters where if
            between two queries, certain rows are removed from the dataset,
            no items are missed from the dataset when changing page

        Returns:
            A dictionary with the following values:
                index: Index of the first item in the current page
                next_index: Index of the first item after the last item on
                    the current page
                page_size: The current page size
                    data: The actual page of the dataset
            """
        dataset = self.indexed_dataset()
        assert index is not None and index >= 0 and index <= len(dataset)
        count = 0
        next_index = None
        data = []
        if index:
            idx = index
        else:
            idx = 0
        for i in dataset.keys():
            if i >= idx and count < page_size:
                data.append(dataset.get(i))
                count += 1
                continue
            if count == page_size:
                next_index = i
                break
        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index,
        }
