def message(txt):
    mesBox = QMessageBox()
    mesBox.setText(txt)
    mesBox.show()
    mesBox.exec()

def add_note():
    note_name, ok = QInputDialog.getText(win,'Добавить заметку','Название заметки:')
    if ok and note_name != '':
        data[note_name] = {'Текст:': '','Теги':[]}
        notesList.addItem(note_name)
        tagsList.addItems(data[note_name]['Теги'])

def show_note():
    key = notesList.selectedItems()[0].text()
    textEdit.setText(data[key]['Текст:'])
    tagsList.clear()
    tagsList.addItems(data[key]['Теги'])

def save_note():
    if notesList.selectedItems():
        key = notesList.selectedItems()[0].text()
        data[key]['Текст:'] = textEdit.toPlainText()
        with open('Data.json','w')as file:
            json.dump(data, file, sort_keys=True)
    else:
        message('вы не выбрали заметку!')

def deal_note():
    if notesList.selectedItems():
        key = notesList.selectedItems()[0].text()
        del data[key]
        notesList.clear()
        tagsList.clear()
        textEdit.clear()
        notesList.addItems(data)
        with open('Data.json','w')as file:
            json.dump(data, file, sort_keys=True)
    else:
        message('вы не выбрали заметку!')

def add_tag():
    if notesList.selectedItems():
        key = notesList.selectedItems()[0].text()
        tag = lineEdit.text()
        if not tag in data [key]['Теги']:
            data[key]['Теги'].append(tag)
            lineEdit.clear()
        with open('Data.json','w')as file:
            json.dump(data, file, sort_keys=True)
    else:
        message('вы не выбрали тег!')

def del_tag():
    if tagsList.selectedItems():
        key = notesList.selectedItems()[0].text()
        tag = tagsList.selectedItems()[0].text()
        data[key]['Теги'].remove(tag)
        tagsList.clear()
        tagsList.addItems(data[key]['Теги'])
        with open('Data.json','w')as file:
            json.dump(data, file, sort_keys=True)
    else:
        message('вы не выбрали тег!')

def search_tag():
    tag = lineEdit.text()
    if search_tag_btn.text() == 'искать по тегу' and not(tag in ['',' ']):
        notes_filtered = {}
        for note in data:
            if tag in data[note]['Теги']:
                notes_filtered[note]=data[note]
        search_tag_btn.setText('Сбросить поиск')
        notesList.clear()
        tagsList.clear()
        notesList.addItems(notes_filtered)
    elif search_tag_btn.text() == 'Сбросить поиск':
        lineEdit.clear()
        notesList.clear()
        tagsList.clear()
        notesList.addItems(data)
        search_tag_btn.setText('искать по тегу')
    else:
        message('вы не ввели тег!')

import json
'''data = {
        ' о планетах' : {
                        'Текст:' : 'что елси вода на марсе это признак жизни?',
                        'Теги' : ['Марс', 'Гипоезы']
                        },
        'О черных дырах':{
                        'Текст:' : ' Сингулярность на горизонте событий отсуствует ',
                        'Теги':['черные дыры', 'факты']
                        }
}
with open('Data.json','w', encoding= 'utf-8')as file:
    json.dump(data, file , sort_keys=True)

def load_notes():
    with open('Data.json','r', encoding= 'utf-8')as file:
        notes = json.load(file)
    notesList.clear()
    notesList.addItems(notes.keys())'''

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QLineEdit,
    QTextEdit,
    QInputDialog,
    QMessageBox
    )

k = 0,8
app = QApplication([])
win = QWidget()
win.setWindowTitle('Умные заметки')
win.resize(1000,500)

#Виджеты
textEdit = QTextEdit()
notesList = QListWidget()
tagsList = QListWidget()
lineEdit = QLineEdit()
save_note_btn = QPushButton('Сохранить заметки')
deal_note_btn = QPushButton('Удалить заметку')
add_note_btn = QPushButton('Добавить заметку')
add_tag_btn = QPushButton('Добавить тег')
del_tag_btn = QPushButton('Удалить тег')
search_tag_btn = QPushButton('искать по тегу')


main_lain = QHBoxLayout()
left_lain = QVBoxLayout()
right_line =  QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()
line5 = QHBoxLayout()
line6 = QHBoxLayout()
line7 = QHBoxLayout()

line1.addWidget(notesList)
line2.addWidget(add_note_btn)
line2.addWidget(deal_note_btn)
line3.addWidget(save_note_btn)
line4.addWidget(tagsList)
line5.addWidget(lineEdit)
line6.addWidget(del_tag_btn)
line6.addWidget(add_tag_btn)
line7.addWidget(search_tag_btn)

right_line.addLayout(line1)
right_line.addLayout(line2)
right_line.addLayout(line3)
right_line.addLayout(line4)
right_line.addLayout(line5)
right_line.addLayout(line6)
right_line.addLayout(line7)

left_lain.addWidget(textEdit)

main_lain.addLayout(left_lain,60)
main_lain.addLayout(right_line, 60)

win.setLayout(main_lain)

add_note_btn.clicked.connect(add_note)
notesList.itemClicked.connect(show_note)
save_note_btn.clicked.connect(save_note)
deal_note_btn.clicked.connect(deal_note)
add_tag_btn.clicked.connect(add_tag)
del_tag_btn.clicked.connect(del_tag)
search_tag_btn.clicked.connect(search_tag)

with open('Data.json','r')as file:
    data = json.load(file)
notesList.addItems(data)

win.show()
app.exec_()
