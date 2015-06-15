from check_dell import parse_om

class storage:
    
    @classmethod
    def controllers():
        map(controller, parse_om("storage controller"))

    class controller:
        vdisks = lambda self: parse_om("storage vdisk controller=%s" % (self.ID))
        pdisks = lambda self: parse_om("storage pdisk controller=%s" % (self.ID))
        battery = lambda self: parse_om("storage battery controller=%s" % (self.ID))

        def __init__(self, props):
            for x, y in props.items():
                self.__setattr__(x, y)

        def __repr__(self):
            return "Controller #%s" % self.ID