class Table:
    def __init__(self, row, col):
        table = list()
        self.table = table
        self.row = row
        self.col = col
        for _ in range(self.row):
            rw = list()
            for _ in range(self.col):
                rw.append(0)
            table.append(rw)

    def add_row(self, row):
        row_1 = list()
        for _ in range(self.col):
            row_1.append(0)
        self.table.insert(row, row_1)
        self.row += 1
        # print(self.table)

    def add_col(self, col):
        table_1 = list()
        for i in self.table:
            i.insert(col, 0)
            table_1.append(i)
        self.table = table_1
        self.col += 1

    def get_value(self, row, col):
        if 0 <= row < self.row and 0 <= col < self.col:
            return self.table[row][col]
        else:
            return None

    def set_value(self, row, col, value):
        self.table[row][col] = value

    def n_rows(self):
        return self.row

    def n_cols(self):
        return self.col

    def delete_col(self, col):
        table_1 = list()
        for i in self.table:
            del i[col]
            table_1.append(i)
        self.table = table_1
        self.col -= 1

    def delete_row(self, row):
        del self.table[row]
        self.row -= 1
