""" STM Metro Client """

import xml.etree.cElementTree as et

import requests

LINE_COLOR = {
    1: 'Green',
    2: 'Orange',
    4: 'Yellow',
    5: 'Blue'
}

class StmMetroClient():
    """Define Metro Client"""
    def __init__(self):
        self.url = 'http://www2.stm.info/1997/alertesmetro/esm.xml'
        self.data = None
        self._line = None

    def get_state(self):
        """Get state"""
        response = requests.get(self.url)
        res = [dict((attr.tag, attr.text) for attr in el) for
               el in et.fromstring(response.content)]
        self.data = res
        return res

    def get_state_by_line(self, line):
        """Get state by line. line = number or color"""
        if isinstance(line, int):
            self._line = line
        elif isinstance(line, str):
            self._line = self.get_line_number_by_color(line)
        response = self.get_state()
        for line_result in response:
            if int(line_result['NoLigne']) == self._line:
                return line_result
        return None

    @staticmethod
    def get_lines():
        return LINE_COLOR

    @staticmethod
    def get_line_number_by_color(line_color):
        """Get line number by color"""
        for line in LINE_COLOR:
            if line_color == LINE_COLOR[line]:
                return line
        return None

    @staticmethod
    def get_line_color_by_number(line_number):
        """Get line color by number"""
        return LINE_COLOR[line_number]
