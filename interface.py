from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QLineEdit
from PySide6.QtGui import QCloseEvent, QPixmap
from from_dec import *
from to_dec import *


class LoginWindow(QWidget):
    """Class responsible for displaying the window, receiving data from text fields, displaying data,
    communicating with the user, calling functions responsible for calculations"""

    def __init__(self, width, height):
        """Declaring text fields, and window size"""
        super().__init__()

        # text fields
        self.dec_line_edit = QLineEdit(self)
        self.bin_line_edit = QLineEdit(self)
        self.oct_line_edit = QLineEdit(self)
        self.hex_line_edit = QLineEdit(self)

        # window size parameters
        self.window_width = width
        self.window_height = height

        self.setup()

    def setup(self):
        """Method defining basic elements displayed in the application, displaying graphics, text fields,
         defining their position, creating buttons, displaying the window itself"""

        # displaying the title graphics
        pix_title = QLabel(self)
        title = QPixmap('./pixmaps/Title.png')
        pix_title.setPixmap(title)
        # declaring position on the window
        pix_title.move((self.window_width-title.width())/2, 0)

        # displaying graphics to all numeral systems text fields
        pix_dec = QLabel(self)
        dec_map = QPixmap('./pixmaps/Dec.png')
        pix_dec.setPixmap(dec_map)
        # declaring position on the window
        dec_height_position = title.height()
        pix_dec.move((self.window_width-dec_map.width())/2, dec_height_position)

        pix_bin = QLabel(self)
        bin_map = QPixmap('./pixmaps/Bin.png')
        pix_bin.setPixmap(bin_map)
        # declaring position on the window
        pix_bin.move((self.window_width-bin_map.width())/2, dec_height_position+100)

        pix_oct = QLabel(self)
        oct_map = QPixmap('./pixmaps/Oct.png')
        pix_oct.setPixmap(oct_map)
        # declaring position on the window
        pix_oct.move((self.window_width-oct_map.width())/2, dec_height_position+200)

        pix_hex = QLabel(self)
        hex_map = QPixmap('./pixmaps/Hex.png')
        pix_hex.setPixmap(hex_map)
        # declaring position on the window
        pix_hex.move((self.window_width-hex_map.width())/2, dec_height_position+300)

        # Displaying text fields on the window
        text_field_width = 300
        text_field_height = 50

        # set size and positions to all text fields
        self.dec_line_edit.setFixedSize(text_field_width, text_field_height)
        self.dec_line_edit.move((self.window_width-text_field_width)/2, 100)

        self.bin_line_edit.setFixedSize(text_field_width, text_field_height)
        self.bin_line_edit.move((self.window_width-text_field_width)/2, 200)

        self.oct_line_edit.setFixedSize(text_field_width, text_field_height)
        self.oct_line_edit.move((self.window_width-text_field_width)/2, 300)

        self.hex_line_edit.setFixedSize(text_field_width, text_field_height)
        self.hex_line_edit.move((self.window_width-text_field_width)/2, 400)

        # Displaying buttons
        licz_btn = QPushButton("CALCULATE", self)
        licz_btn.setFixedSize(100, 50)
        licz_btn.move(150, 480)

        quit_btn = QPushButton("QUIT", self)
        quit_btn.move(5, 570)

        # Checking the status of the buttons
        quit_btn.clicked.connect(QApplication.instance().quit)
        licz_btn.clicked.connect(self.licz)

        # Displaying the window
        self.setFixedSize(self.window_width, self.window_height)
        self.setWindowTitle("NUMERAL SYSTEMS")
        self.show()

        self.cursor_zero()

    def licz(self):
        """Method that checks the active text field and calls the corresponding methods to perform the calculation"""

        # Positioning the cursor at zero position
        cursor_act = self.cursor_select()
        line_choose = 0

        # Selecting a text field
        for i in range(4):
            if cursor_act[i] != 0:
                break
            else:
                line_choose += 1

        # Execution of operations for a selected text field
        if line_choose == 0:
            fail = self.imp_fail(line_choose)
            if fail == 0:
                self.inp_dec()

        if line_choose == 1:
            val = self.bin_line_edit.text()
            fail = self.imp_fail(line_choose)

            if fail == 0:
                bin_val = self.inp_bin_oct(val, line_choose)

                self.dec_line_edit.setText(bin_val)
                self.inp_dec()

        if line_choose == 2:
            val = self.oct_line_edit.text()
            fail = self.imp_fail(line_choose)

            if fail == 0:
                oct_val = self.inp_bin_oct(val, line_choose)

                self.dec_line_edit.setText(oct_val)
                self.inp_dec()

        if line_choose == 3:
            val = self.hex_line_edit.text()
            fail = self.imp_fail(line_choose)

            if fail == 0:
                hex_val = self.imp_hex(val)

                self.dec_line_edit.setText(hex_val)
                self.inp_dec()

        self.cursor_zero()

    def cursor_select(self):
        """Method to read the cursor position for all text fields"""

        line_dec = self.dec_line_edit.cursorPosition()
        line_bin = self.bin_line_edit.cursorPosition()
        line_oct = self.oct_line_edit.cursorPosition()
        line_hex = self.hex_line_edit.cursorPosition()

        cursor_every_position = [line_dec, line_bin, line_oct, line_hex]

        return cursor_every_position

    def cursor_zero(self):
        """Method to set the cursor to zero position for all text fields"""

        self.dec_line_edit.setCursorPosition(0)
        self.bin_line_edit.setCursorPosition(0)
        self.oct_line_edit.setCursorPosition(0)
        self.hex_line_edit.setCursorPosition(0)

    def inp_bin_oct(self, val, line_set):
        """Method calling appropriate functions performing calculations for binary and octal systems"""
        val = list(val)
        val_trans = []
        val_f = 0

        for i in range(len(val)):
            op1 = int(val[i])
            val_trans.append(op1)

        if line_set == 1:
            val_f = bin_to_dec(val_trans)
        if line_set == 2:
            val_f = oct_to_dec(val_trans)

        val_f_int = int(val_f)
        val_f_str = str(val_f_int)

        return val_f_str

    def inp_dec(self):
        """Method calling appropriate functions performing calculations for decimal system"""

        inp_val = self.dec_line_edit.text()
        inp_val = int(inp_val)

        bin_val = dec_to_bin(inp_val)
        self.bin_line_edit.setText(bin_val[1])

        oct_val = dec_to_oct(inp_val)
        self.oct_line_edit.setText(oct_val[1])

        hex_val = dec_to_heks(inp_val)
        self.hex_line_edit.setText(hex_val[1])

    def imp_hex(self, val):
        """Method calling appropriate functions performing calculations for hexadecimal system"""

        val = list(val)

        val_f = []

        for i in range(len(val)):
            x = val[i]

            for n in range(len(lit_ord)):
                if ord(x) == lit_ord[n] or ord(x) == lit_ord[n]+32:
                    val_f.append(chr(lit_ord[n]))

            for n in range(len(num_ord)):
                if ord(x) == num_ord[n]:
                    val_f.append(int(x))

        dec_val = int(heks_to_dec(val_f))

        dec_val = str(dec_val)

        return dec_val

    def imp_fail(self, line_set):
        """Method to check the correct entry of values into text fields, returns 1 when value is wrong"""

        fail_list = []

        # Fail checking for subsequent lines
        if line_set == 0:
            text_dec = self.dec_line_edit.text()
            text_dec = list(text_dec)

            # The first value must not be 0
            if ord(text_dec[0]) == 48:
                fail_list.append(1)
            else:
                for i in range(len(text_dec)):
                    fail_list.append(1)

                for i in range(len(text_dec)):
                    for n in range(len(num_ord)):
                        # Checking if the value belongs to those considered by the system, num_ord is found in to_dec.py
                        if ord(text_dec[i]) == num_ord[n]:
                            fail_list[i] = 0

        if line_set == 1:
            text_bin = self.bin_line_edit.text()
            text_bin = list(text_bin)

            if ord(text_bin[0]) == 48:
                fail_list.append(1)
            else:
                for i in range(len(text_bin)):
                    fail_list.append(1)

                for i in range(len(text_bin)):
                    for n in range(2):
                        if ord(text_bin[i]) == num_ord[n]:
                            fail_list[i] = 0

        if line_set == 2:
            text_oct = self.oct_line_edit.text()
            text_oct = list(text_oct)

            if ord(text_oct[0]) == 48:
                fail_list.append(1)
            else:
                for i in range(len(text_oct)):
                    fail_list.append(1)

                for i in range(len(text_oct)):
                    for n in range(8):
                        if ord(text_oct[i]) == num_ord[n]:
                            fail_list[i] = 0

        if line_set == 3:
            text_hex = self.hex_line_edit.text()
            text_hex = list(text_hex)

            if ord(text_hex[0]) == 48:
                fail_list.append(1)
            else:
                for i in range(len(text_hex)):
                    fail_list.append(1)

                for i in range(len(text_hex)):
                    for n in range(len(num_ord)):
                        if ord(text_hex[i]) == num_ord[n]:
                            fail_list[i] = 0
                    for m in range(len(lit_ord)):
                        # Checking if the value belongs to those considered by the system, lit_ord is found in to_dec.py
                        if ord(text_hex[i]) == lit_ord[m] or ord(text_hex[i]) == lit_ord[m]+32:
                            fail_list[i] = 0

        # Checks whether fails have been detected
        if 1 in fail_list:
            fail = 1
        else:
            fail = 0

        if fail == 1:
            self.fail_event()

        return fail

    def fail_event(self):
        # Method displaying an error message

        fail_box = QMessageBox()
        fail_box.setText("Incorrect data was entered, please try again")
        fail_box.setIconPixmap(QPixmap('./pixmaps/fail.png'))
        fail_box.exec()

    def keyPressEvent(self, event):
        """A method that checks if the "ENTER" key has been pressed so that calculations can be started from the
        keyboard, the code of the "ENTER" key is checked"""

        if event.key() == 16777220:
            self.licz()

    def closeEvent(self, event: QCloseEvent):
        """A method for closing the application, asking the user if they are sure they want to do this"""

        should_close = QMessageBox.question(self, "Close App", "For sure?",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if should_close == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
