import platform

def general():
    info = dict()

    System_details = platform.platform()

    info["platform details"] = System_details

    system_name = platform.system()

    info["system name"] = system_name

    processor_name = platform.processor()

    info["processor name"] = processor_name

    architecture_details = platform.architecture()

    info["architectural detail"] = architecture_details

    for i, j in info.items():
        print(i, " - ", j)
