from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QLineEdit
from PySide6.QtGui import QCloseEvent, QPixmap
from from_dec import *
from to_dec import *

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.dec_line_edit = QLineEdit(self)
        self.bin_line_edit = QLineEdit(self)
        self.oct_line_edit = QLineEdit(self)
        self.hex_line_edit = QLineEdit(self)

        self.setup()

    def setup(self):
        # Wyswietlanie pixmap
        pix_title = QLabel(self)
        title = QPixmap("F:\BARTEK\PROGRAMING\systemy_liczb\pixmaps\Title.png")
        pix_title.setPixmap(title)
        pix_title.move(20, 0)

        pix_dec = QLabel(self)
        dec_map = QPixmap("F:\BARTEK\PROGRAMING\systemy_liczb\pixmaps\Dec.png")
        pix_dec.setPixmap(dec_map)
        pix_dec.move(140, 50)

        pix_bin = QLabel(self)
        bin_map = QPixmap("F:\BARTEK\PROGRAMING\systemy_liczb\pixmaps\Bin.png")
        pix_bin.setPixmap(bin_map)
        pix_bin.move(150, 150)

        pix_oct = QLabel(self)
        oct_map = QPixmap("F:\BARTEK\PROGRAMING\systemy_liczb\pixmaps\Oct.png")
        pix_oct.setPixmap(oct_map)
        pix_oct.move(160, 250)

        pix_hex = QLabel(self)
        hex_map = QPixmap("F:\BARTEK\PROGRAMING\systemy_liczb\pixmaps\Hex.png")
        pix_hex.setPixmap(hex_map)
        pix_hex.move(110, 350)

        # Ustawienie pol tekstowych w aplikacji
        self.dec_line_edit.setFixedSize(300, 50)
        self.dec_line_edit.move(50, 100)

        self.bin_line_edit.setFixedSize(300, 50)
        self.bin_line_edit.move(50, 200)

        self.oct_line_edit.setFixedSize(300, 50)
        self.oct_line_edit.move(50, 300)

        self.hex_line_edit.setFixedSize(300, 50)
        self.hex_line_edit.move(50, 400)

        licz_btn = QPushButton("CALCULATE", self)
        licz_btn.setFixedSize(100, 50)
        licz_btn.move(150, 480)

        quit_btn = QPushButton("QUIT", self)
        quit_btn.move(5, 570)

        quit_btn.clicked.connect(QApplication.instance().quit)
        licz_btn.clicked.connect(self.licz)

        self.setFixedSize(400, 600)
        self.setWindowTitle("systemy")
        self.show()

        self.cursor_zero()

    def licz(self):
        cursor_act = self.cursor_select()
        line_choose = 0

        for i in range(4):
            if cursor_act[i] != 0:
                break
            else:
                line_choose += 1

        if line_choose == 0:
            fail = self.imp_fail(line_choose)
            if fail == 0:
                self.inp_dec()

        if line_choose == 1:
            val = self.bin_line_edit.text()
            fail = self.imp_fail(line_choose)

            if fail == 0:
                bin_val = self.imp_bo(val, line_choose)

                self.dec_line_edit.setText(bin_val)
                self.inp_dec()

        if line_choose == 2:
            val = self.oct_line_edit.text()
            fail = self.imp_fail(line_choose)

            if fail == 0:
                oct_val = self.imp_bo(val, line_choose)

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
        line_dec = self.dec_line_edit.cursorPosition()
        line_bin = self.bin_line_edit.cursorPosition()
        line_oct = self.oct_line_edit.cursorPosition()
        line_hex = self.hex_line_edit.cursorPosition()

        cursor_every_position = [line_dec, line_bin, line_oct, line_hex]

        return cursor_every_position

    def cursor_zero(self):
        self.dec_line_edit.setCursorPosition(0)
        self.bin_line_edit.setCursorPosition(0)
        self.oct_line_edit.setCursorPosition(0)
        self.hex_line_edit.setCursorPosition(0)

    def imp_bo(self, val, line_set):
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
        inp_val = self.dec_line_edit.text()
        inp_val = int(inp_val)

        bin_val = dec_to_bin(inp_val)
        self.bin_line_edit.setText(bin_val[1])

        oct_val = dec_to_oct(inp_val)
        self.oct_line_edit.setText(oct_val[1])

        hex_val = dec_to_heks(inp_val)
        self.hex_line_edit.setText(hex_val[1])

    def imp_hex(self, val):
        val = list(val)

        val_f = []
        dec_val = ''

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

        fail_list = []

        if line_set == 0:
            text_dec = self.dec_line_edit.text()
            text_dec = list(text_dec)

            if ord(text_dec[0]) == 48:
                fail_list.append(1)
            else:
                for i in range(len(text_dec)):
                    fail_list.append(1)

                for i in range(len(text_dec)):
                    for n in range(len(num_ord)):
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
                        if ord(text_hex[i]) == lit_ord[m] or ord(text_hex[i]) == lit_ord[m]+32:
                            fail_list[i] = 0

        if 1 in fail_list:
            fail = 1
        else:
            fail = 0

        if fail == 1:
            self.fail_event()

        return fail

    def fail_event(self):
        fail_box = QMessageBox()
        fail_box.setText("Incorrect data was entered, please try again")
        fail_box.setIconPixmap(QPixmap("F:\BARTEK\PROGRAMING\systemy_liczb\pixmaps/fail.png"))
        fail_box.exec()

    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.licz()

    def closeEvent(self, event: QCloseEvent):
        should_close = QMessageBox.question(self, "Close App", "For sure?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if should_close == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()