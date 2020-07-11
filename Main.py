from Utils.Exceptions import GeneralException
from App.Application import Application
from Utils.Exceptions import ErrorCodes
import traceback
import os

def isOsSupported():
    if os.name == "nt" or os.name == "posix":
        return
    else:
        raise OSError()

def main():
    try:
        isOsSupported
        app = Application()
        app.run()
    except GeneralException as gError:
        print(str(gError))
        exit(gError._code.value)
    except Exception as Error:
        traceback.print_exc()
        exit(int(ErrorCodes.INTERNAL_ERROR))
    finally:
        pass

if __name__ == "__main__":
    main()
    