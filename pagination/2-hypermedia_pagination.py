#!/usr/bin/env python3
'''Simple pagination that returns a dictionary'''
from ast import Dict
import csv
import math
from typing import List


class Server:
    '''Server class to paginate a database of popular baby names.'''
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        '''Cached dataset'''

        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Returns the appropriate page of the dataset
        (i.e. the correct list of rows)'''
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        indexes = index_range(page, page_size)

        start = indexes[0]
        end = indexes[1]

        ds = self.dataset()

        return (ds[start:end])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        ''''Returns a dictionary containing the following key-value pairs:'''
        page_data = self.get_page(page, page_size)

        page_info = {
            "page_size": page_size,
            "page": page,
            "data": page_data,
            "next_page": page + 1 if len(page_data) == page_size else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": math.ceil(len(self.dataset()) / page_size)
        }

        return page_info


def index_range(page: int, page_size: int) -> tuple:
    '''simple helper function'''
    end = page * page_size
    start = end - page_size
    return (start, end)
