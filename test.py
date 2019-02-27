"""Tests"""
import sys
from datetime import datetime, timedelta
from os import remove

from stm_metro_client import StmMetroClient


def test():
    """Test function"""
    rcode = 0
    stm_client = StmMetroClient()
    api_time_start = datetime.now()
    print(stm_client.get_state())
    api_time_end = datetime.now()

    print('API request took '
          + str((api_time_end - api_time_start).total_seconds())
          + ' seconds to complete.')

    quit(rcode)

test()
