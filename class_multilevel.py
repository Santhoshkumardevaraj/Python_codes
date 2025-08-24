class Category():
    def showcategory(self):
        print("Category")

class SubCategory(Category):
    def showsubcategory(self):
        print("sub Category")

class Child(SubCategory):
    def __init__(self):
        print('Child')


obj_child=Child()
obj_child.showsubcategory()
obj_child.showcategory()