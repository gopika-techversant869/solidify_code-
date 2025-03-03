'''--------------Scenario: User Roles in a Web Application------------------------
Imagine you are building a web application where users can have different roles:

-> Admin - Can view, edit, and delete content.
-> Editor - Can view and edit, but not delete content.
-> Viewer - Can only view content.'''

class User:
    def view_content(self):
        print("Viewing content")

    def edit_content(self):
        print("Editing content")

    def delete_content(self):
        print("Deleting content")

class Admin(User):
    pass  

class Editor(User):
    def delete_content(self):
        raise Exception("Editors cannot delete content!") 
class Viewer(User):
    def edit_content(self):
        raise Exception("Viewers cannot edit content!") 

    def delete_content(self):
        raise Exception("Viewers cannot delete content!")  
    

# Creating users
admin = Admin()
editor = Editor()
viewer = Viewer()

admin.delete_content()  
editor.delete_content() 
viewer.edit_content()  
