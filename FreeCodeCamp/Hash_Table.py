class HashTable:
    def __init__(self):
        self.collection = {}
    def hash(self,string):
        hash_value = 0
        for char in string:
            hash_value += ord(char)
        return hash_value
    def add(self,key,value):
        hash_value = self.hash(key)
        if hash_value not in self.collection.keys():
            self.collection[hash_value] = {key:value}
        else:
            self.collection[hash_value].update({key:value})
    def remove(self,key):
        hash_value = self.hash(key)
        if hash_value in self.collection.keys():
            if key in self.collection[hash_value]:
                del self.collection[hash_value][key]
            print(hash_value)
        else:
            return
    def lookup(self,key):
        hash_value = self.hash(key)
        if hash_value in self.collection.keys():
            if key in self.collection[hash_value]:
                return (self.collection[hash_value][key])
            return
        return

    def show(self):
        print(self.collection)
        return
obj = HashTable()
obj.add('golf', 'sport')
obj.add('read', 'book')
obj.add('dear', 'friend')
obj.show()
#obj.remove('clear')
#obj.remove("golf")
obj.lookup('golf')
obj.remove("clear")
obj.show()
