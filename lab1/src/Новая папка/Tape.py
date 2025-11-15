class Tape:
    def __init__(self, word: str):
        # храним ленту как список символов
        self._cells = list(word) if word else ["_"]
        self._head = 0

    def move(self, direction: str):
        if direction == "R":
            self._head += 1
            # расширяем ленту вправо при необходимости
            if self._head >= len(self._cells):
                self._cells.append("_")
        elif direction == "L":
            self._head -= 1
            # расширяем ленту слева при уходе за границу
            if self._head < 0:
                self._cells.insert(0, "_")
                self._head = 0
        elif direction == "N":
            # остаемся на месте
            pass
        else:
            # защитимся от неверного направления
            raise ValueError(f"Unknown move direction: {direction}")

    def read_symbol(self) -> str:
        return self._cells[self._head]
    
    def write_symbol(self, sym: str):
        self._cells[self._head] = sym

    def read_word(self) -> str:
        word = "".join(self._cells)
        if not word.startswith("_"):
            word = "_" + word
        if not word.endswith("_"):
            word = word + "_"
        return word

    def clear(self):
        self._cells = ["_"]
        self._head = 0
