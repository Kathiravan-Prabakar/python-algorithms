class HashTable:
    def __init__(self, table_size: int):
        self.table_size = table_size
        self._table = [[] for _ in range(self.table_size)]

    def hashing(self, key) -> int:
        return key % len(self._table)

    def insert(self, keyval, value) -> None:
        key = self.hashing(keyval)
        self._table[key].append(value)

    def display(self) -> None:
        for i in range(len(self._table)):
            print(i, end=" ")
            for j in self._table[i]:
                print(" | ", end=" ")
                print(j, end=" ")
            #print()

    def search(self, key) -> dict:
        try:
            val = self._table[key]
            toret = {"key": key, "val": val}
            return toret
        except Exception as e:
            print(e)

hashTable = HashTable(table_size=1)
hashTable.insert(10, "Chennai")
hashTable.display()
hashTable.search(0)