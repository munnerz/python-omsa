from check_dell import parse_om

class storage:
    controllers = parse_om("storage controller")

    class types:
        vdisk = 'vdisk'
        pdisk = 'pdisk'
        battery = 'battery'