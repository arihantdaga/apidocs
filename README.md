# apidocs
Its a tiny(actually nano) Python module but very handy for learners and experimenters to look for available methods and doc strings on any object. And sometimes even for experts to quickly peek into new modules.

This nano module has only 1 method #get_info(object)
## How to use (example):
```sh
import apidocs as apidocs
myList = [1,2,3,4]
# Lets say i want to see availaible methods on myList
apidocs.get_info(myList)
```
It'll print availaible methods and doc strings on object of list type. 

THAT's ALL.
