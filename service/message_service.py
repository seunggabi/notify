class MessageService:
    def __init__(self, message, step):
        self.message = message
        self.len = len(self.message)

        self.step = step

        self.start = 0
        self.end = 0

        self.item = message[0:step]

    def _rindex(self, key):
        try:
            return self.item.rindex(key)
        except ValueError:
            return -1

    def _index_space(self):
        return max(self._rindex("\n"), self._rindex(" "))

    def _is_step(self):
        return (
            self.len <= self.start + self.step
            or self.item[-1] == "\n"
            or self._rindex("\n") == -1
            or self._rindex(" ") == -1
        )

    def _item(self):
        self.item = self.message[self.start:self.end]

    def _end(self):
        self.end = (
            self.start + self.step
            if self._is_step()
            else self.start + self._index_space()
        )

    def __iter__(self):
        return self

    def __next__(self):
        self.start = self.end

        if self.start >= self.len:
            raise StopIteration

        self._end()
        self._item()

        return self.item
