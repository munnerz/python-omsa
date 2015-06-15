from check_dell import parse_om

def load_props(obj, props):
    obj._props = props
    for x, y in props.items():
        setattr(obj, x, y)

class storage:
    class Controller:
        class PhysicalDisk:
            def __init__(self, props):
                load_props(self, props)

        class VirtualDisk:
            def __init__(self, props):
                load_props(self, props)

        class Battery:
            def __init__(self, props):
                load_props(self, props)

        def _get_properties(self, type):
            return parse_om("storage %s controller=%s" % (type, self.ID))

        def vdisks(self):
            return map(self.__class__.VirtualDisk, self._get_properties('vdisk'))

        def pdisks(self):
            return map(self.__class__.PhysicalDiskisk, self._get_properties('pdisk'))

        def battery(self):
            return map(self.__class__.Battery, self._get_properties('battery'))

        def __init__(self, props):
            load_props(self, props)

        def __repr__(self):
            return "Controller #%s" % self.ID

    @classmethod
    def controllers(cls):
        return map(cls.Controller, parse_om("storage controller"))