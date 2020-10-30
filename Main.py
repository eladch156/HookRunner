from Utils.Exceptions import GeneralException
from App.Application import Application
from Utils.Exceptions import ErrorCodes
import traceback
import os


def _is_os_supported():
    if os.name == "nt" or os.name == "posix":
        return
    else:
        raise OSError()


def main():
    try:
        _is_os_supported
        _app = Application()
        _app.run()
    except GeneralException as general_error:
        print(str(general_error))
        exit(general_error._code.value)
    except Exception as _:
        traceback.print_exc()
        exit(int(ErrorCodes.INTERNAL_ERROR))
    finally:
        pass


if __name__ == "__main__":
    main()
