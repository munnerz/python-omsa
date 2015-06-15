from check_dell import parse_om

class storage:
    class Controller:
        vdisks = lambda self: parse_om("storage vdisk controller=%s" % (self.ID))
        pdisks = lambda self: parse_om("storage pdisk controller=%s" % (self.ID))
        battery = lambda self: parse_om("storage battery controller=%s" % (self.ID))

        def _get_properties(self, type):
            return parse_om("storage %s controller=%s" % (type, self.ID))

        def vdisks(self):
            return self._get_properties('vdisk')

        def pdisks(self):
            return self._get_properties('pdisk')

        def battery(self):
            return self._get_properties('battery')

        def __init__(self, props):
            for x, y in props.items():
                setattr(self, x, y)

        def __repr__(self):
            return "Controller #%s" % self.ID

    @classmethod
    def controllers(cls):
        map(cls.Controller, parse_om("storage controller"))