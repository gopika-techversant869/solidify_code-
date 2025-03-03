class User:
    def view_content(self):
        print("Viewing content")

class Editor(User):
    def edit_content(self):
        print("Editing content")

class Admin(Editor):  
        print("Deleting content")

admin = Admin()
editor = Editor()
viewer = User()

admin.delete_content()  
editor.edit_content()  
viewer.view_content()  
