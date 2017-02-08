import colorama as colorama

def get_info(object, gap=7):
    """ This module prints availaible methods and doc strings
		for strings, list, modules etc given objects.
     """
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = (lambda s: " ".join(s.split())) or (lambda s: s)
    for method in methodList:
    	method_name = str("%s: " %(method.ljust(gap)))
    	method_desc= str("%s" %(processFunc(str(getattr(object, method).__doc__))))
    	color = colorama.Fore.YELLOW if method_name.startswith("__") else colorama.Fore.GREEN
    	print(color + method_name + colorama.Fore.BLACK + method_desc + "\n")

if __name__ == "__main__":
    print info.__doc__
