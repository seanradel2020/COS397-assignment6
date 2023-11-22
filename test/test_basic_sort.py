# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

import pytest
import numpy as np
from basic_sort_IMSG.int_sort import bubble, quick, insertion

def is_sorted(int_list):
    """
    :param int_list: a list of integers

    :returns: true if sorted, else false
    """
    return all(int_list[i] <= int_list[i + 1] for i in range(len(int_list) - 1))


@pytest.fixture
def int_lists():
    # fixture which creates testing data for all tests
    return [[3, 2, 1], [1, 1, 1], np.random.randint(low=-10, high=200, size=5)]


def test_bubble(int_lists):
    for unsorted_list in int_lists:
        sorted_list = bubble(unsorted_list)
        assert is_sorted(sorted_list)


def test_quick(int_lists):
    for unsorted_list in int_lists:
        sorted_list = quick(unsorted_list)
        assert is_sorted(sorted_list)


def test_insertion(int_lists):
    for unsorted_list in int_lists:
        sorted_list = insertion(unsorted_list)
        assert is_sorted(sorted_list)
