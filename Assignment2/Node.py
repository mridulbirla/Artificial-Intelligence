__author__ = 'mridul'


class Node:

    def __init__(self,identifier):

        self.val=identifier
        self.children=[]

    def add_children(self,child):

        self.children.append(child)

    def get_children(self):
        return self.children



