"""Tests"""

from datetime import datetime

from stm_metro_client import stm_metro_client


def test():
    """Test function"""
    rcode = 0
    stm_client = stm_metro_client.StmMetroClient()
    api_time_start = datetime.now()
    print(stm_client.get_state())
    api_time_end = datetime.now()

    print('API request took '
          + str((api_time_end - api_time_start).total_seconds())
          + ' seconds to complete.')

    quit(rcode)


test()
