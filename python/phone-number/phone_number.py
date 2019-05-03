import re

class Phone(object):
    def __init__(self, phone_number):
        m = re.search('(?!1)(?P<area>[1-9][0-9]{2})(\-|\.|\ |\))*(?P<exchange>[2-9][0-9]{2})(\-|\.|\ )*(?P<personal>[0-9]{4,})', phone_number)
        if not m:
            raise ValueError("No number found inside !!!")
        result = ''.join([m.group('area'), m.group('exchange'), m.group('personal')])
        if not len(result) == 10:
            raise ValueError("the number is too long")
        self.number = result
        self.pretty_number = '(' + m.group('area') + ') ' + m.group('exchange') + '-' + m.group('personal')
        self.area_code = m.group('area')
        pass
    
    def pretty(self):
        return self.pretty_number

