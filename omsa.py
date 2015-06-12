from check_dell import parse_om

class storage:

    class controllers:
        def list():
            return parse_om("storage controller", ["ID"])

    class types:
        vdisk = 'vdisk'
        pdisk = 'pdisk'
        battery = 'battery'