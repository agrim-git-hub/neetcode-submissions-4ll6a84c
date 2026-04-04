from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #creating the dictionary using default dict
        rows = defaultdict(set)
        columns = defaultdict(set)
        SM = defaultdict(set)

        for row in range(9):
            for column in range(9):
                val = board[row][column] # getting value at index(row,column)

                if val =='.':
                    continue

                #checking if the value exists in either of the 3 dictionaries. If value exists, then it violates the rules of a valid sudoku
                elif val in rows[row] or val in columns[column] or val in SM[(row//3,column//3)]:
                    return False
                #if not already present, this number is added to each of the 3 dictionaries storing its availibility in which row, column and sub matrix
                else:
                    rows[row].add(val)
                    columns[column].add(val)
                    SM[(row//3,column//3)].add(val)
                
            #if the whole board is iterated wihtout throwing errors return True
        return True


