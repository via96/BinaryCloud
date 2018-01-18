import hashlib
import paramiko
import os

FILEPATH = '/home/developer/develop/Projects/libs(backup)/'


class Directory:

    def __init__(self, path):
        self.filepath = path

    filepath = ''
    hashList = []

    def get_hash(self, path):
        with open(path, 'rb') as f:
            m = hashlib.md5()
            while True:
                data = f.read(8192)
                if not data:
                    break
                m.update(data)
            return m.hexdigest()

    def find_files(self, catalog):
        find_files = []
        for root, dirs, files in os.walk(catalog):
            find_files += [os.path.join(root, name) for name in files]
        return find_files

    def load(self):
        list = []
        for file in self.find_files(self.filepath):
            list += [file, self.get_hash(file)]
        return list

    def update(self):
        self.hashList = self.load()

    def isUpdated(self):
        return self.hashList != self.load()


dir = Directory(FILEPATH)
dir.update()
while True:
    if dir.isUpdated():
        print('Update')
