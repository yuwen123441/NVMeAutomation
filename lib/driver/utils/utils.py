



def print_structure(in_put):
    for item in in_put._fields_:
        attr = item[0]
        value = getattr(in_put, attr)
        type_ = type(value).__name__
        if "Array" in type_:
            if "byte" in type_ or "uint" in type_:
                content_list = ["{:#04x}".format(x) for x in value]
                print("{}: {}".format(attr, content_list))
            elif "DataStructure" in type_:
                for index, value_ in enumerate(value):
                    print("{}: array index at:{}".format(type_, index))
                    print_structure(value_)
        elif "int" in type_ or "long" in type_:
            print("{}: {}".format(attr, value))
        else:
            print_structure(value)