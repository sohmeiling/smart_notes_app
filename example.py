from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QTextEdit, QListWidget, QLabel,
    QPushButton, QLineEdit,
    QHBoxLayout, QVBoxLayout,
    QInputDialog
                             )
app = QApplication([])
window = QWidget()
window.resize(900, 700)
window.setWindowTitle('Smart Notes')

# ------------------------------------------
# Data
notes = {
    "Welcome!" : {
        "text" : "This is the best note taking app in the world!",
        "tags" : ["good", "instructions"]
    }
}

# ------------------------------------------
# Widgets
field_text = QTextEdit()

list_notes_label = QLabel('List of notes')
list_notes = QListWidget()
button_note_create = QPushButton('Create note')
button_note_del = QPushButton('Delete note')
button_note_save = QPushButton('Save note')

list_tags_label = QLabel('List of tags')
list_tags = QListWidget()
field_tag = QLineEdit('')
field_tag.setPlaceholderText('Enter tag...')
field_text = QTextEdit()
button_add = QPushButton('Add to note')
button_del = QPushButton('Untag from note')
button_search = QPushButton('Search notes by tag')

# ------------------------------------------
# Layouts
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout() #Putting create and delete buttons in one row
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
col_2.addLayout(row_1)

col_2.addWidget(button_note_save)
col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)

row_2 = QHBoxLayout() #Putting create and delete buttons in one row
row_2.addWidget(button_add)
row_2.addWidget(button_del)
col_2.addLayout(row_2)
col_2.addWidget(button_search)

layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
window.setLayout(layout_notes)

# ------------------------------------------
# Functions

def add_note():
    note_name, ok = QInputDialog.getText(window, "Note name", "Enter the name of the note:")
    if ok and note_name != "":
        notes[note_name] = {"text" : "", "tags" : []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]["tags"])
        print(notes) 

def show_note():
    key = list_notes.selectedItems()[0].text()
    field_text.setText(notes[key]["text"])
    list_tags.clear()
    list_tags.addItems(notes[key]["tags"])

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["text"] = field_text.toPlainText()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print("No selected note")


# ------------------------------------------
# Event handling
button_note_create.clicked.connect(add_note)
list_notes.itemClicked.connect(show_note)
button_note_save.clicked.connect(save_note)


# ------------------------------------------
# Execution of the application

window.show()
with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)

app.exec_()



