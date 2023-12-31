class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row_check = self.valid_rows(board)
        column_check = self.valid_rows(self.transpose(board))
        sub_box_check = self.valid_rows(self.group_by_sub_box(board))
        return row_check and column_check and sub_box_check
    
    def transpose(self, board: list[list[str]]) -> list[list[str]]:
        transposed = [row.copy() for row in board]
        for i in range(len(board)):
            for j in range(len(board[i])):
                transposed[i][j] = board[j][i]
        return transposed

    def group_by_sub_box(self, board: list[list[str]]) -> list[list[str]]:
        sub_box = []
        for sub in range(0,7,3):
            section = [[], [], []]
            for i in range(3):
                for j in range(9):
                    if j < 3:
                        section[0].append(board[sub + i][j])
                    elif j < 6:
                        section[1].append(board[sub + i][j])
                    else:
                        section[2].append(board[sub + i][j])
            sub_box.extend(section)
        return sub_box
    
    def valid_rows(self, board: list[list[str]]) -> bool:
        for row in board:
            numbers = set()
            for number in row:
                if number == ".":
                    continue
                if number in numbers:
                    return False
                else:
                    numbers.add(number)
        return True
    

board1 = \
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board2 = \
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board3 = \
[[".",".",".",".",".",".","5",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,["9","3",".",".","2",".","4",".","."]
,[".",".","7",".",".",".","3",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".","3","4",".",".",".","."]
,[".",".",".",".",".","3",".",".","."]
,[".",".",".",".",".","5","2",".","."]]

