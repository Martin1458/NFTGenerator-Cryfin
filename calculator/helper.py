def pprint(obj):
    nameOfVar = [name for name in globals() if globals()[name] is obj]
    print("{}: {}".format(str(nameOfVar), obj))
    exit()

