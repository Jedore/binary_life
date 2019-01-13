"""
    @author: Jedore
    @project: binary_life
    @file: converters.py
    @time: 11/9/2018 1:53 PM
    
"""


class BoolConverter:
    regex = "(True)|(False)"
    
    @staticmethod
    def to_python(value):
        return False if value == 'False' else True
    
    @staticmethod
    def to_url(value):
        return str(value)
