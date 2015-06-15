from check_dell import parse_om

class storage:
    controllers = parse_om("storage controller", ["ID"])

    class types:
        vdisk = 'vdisk'
        pdisk = 'pdisk'
        battery = 'battery'