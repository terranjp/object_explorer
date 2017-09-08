import sys
import traceback

from PyQt5.QtWidgets import QApplication

from example_data import example_dict
from widgets.objectexplorer import ObjectExplorer


def handleException(exc_type, exc_value, exc_traceback):
    traceback.print_exception(exc_type, exc_value, exc_traceback)

sys.excepthook = handleException


def main(data=None):
 
    app = QApplication(sys.argv)

    explorer = ObjectExplorer(data=data)
    explorer.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main(example_dict)
