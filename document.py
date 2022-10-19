"""
This module helps to define a document.
.. since: 0.2
"""

# -*- coding: utf-8 -*-
# MIT License
#
# Copyright (c) 2022 Olivier B. OURA
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


class Document:

    def __init__(self, name, user):
        assert len(str(name)) > 5
        self.name = name
        self.user = user

    def get_title(self):
        db = Database.get_instance()
        row = db.get(self.name)
        return row[0]

    def get_content(self):
        db = Database.get_instance()
        row = db.get(self.name)
        return row[1]

    @staticmethod
    def get_all_documents(cls):
        raise NotImplemented


class User:

    def make_new_document(self, name):
        doc = Document(name, self)
        return doc

    def get_my_documents(self):
        docs = []
        for doc in Document.get_all_documents():
            if doc.user == self:
                docs.append(doc)
        return docs


class Database:

    def get(self, name):
        base = [
            ("Python tutorial", "We learn here Object Oriented Programming in Python"),
            ("Java tutorial", "We learn here Object Oriented Programming in Java"),
            ("NodeJS tutorial", "We learn here Object Oriented Programming in NodeJS"),
        ]
        for doc in base:
            if doc[0] == name:
                return doc
        return None

    @staticmethod
    def get_instance():
        return Database()
