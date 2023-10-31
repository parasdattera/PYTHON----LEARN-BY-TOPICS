
import sys
def linux_interaction():
    assert('linux' in sys.platform),'function can only run on linux system'
    print("do something")


try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print("linus function will not be executed")

