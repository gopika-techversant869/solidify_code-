from abc import ABC, abstractmethod

# Separate interfaces (smaller and specific)
class Viewable(ABC):
    @abstractmethod
    def view_content(self):
        pass

class Editable(ABC):
    @abstractmethod
    def edit_content(self):
        pass

class Deletable(ABC):
    @abstractmethod
    def delete_content(self):
        pass

# Implementing only necessary interfaces
class Admin(Viewable, Editable, Deletable):  # Implements all three
    def view_content(self):
        print("Admin is viewing content")

    def edit_content(self):
        print("Admin is editing content")

    def delete_content(self):
        print("Admin is deleting content")

class Editor(Viewable, Editable):  # Implements only Viewable & Editable
    def view_content(self):
        print("Editor is viewing content")

    def edit_content(self):
        print("Editor is editing content")

class Viewer(Viewable):  # Implements only Viewable
    def view_content(self):
        print("Viewer is viewing content")

# Creating objects
admin = Admin()
editor = Editor()
viewer = Viewer()

admin.view_content()  
admin.edit_content()  
admin.delete_content()  
editor.view_content() 
editor.edit_content()  
# editor.delete_content()  #  Not possible, as Editor doesn't implement Deletable

viewer.view_content()  
# viewer.edit_content()  #  Not possible, as Viewer doesn't implement Editable
# viewer.delete_content()  #  Not possible, as Viewer doesn't implement Deletable
