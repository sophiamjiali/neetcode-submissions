class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Track digit occurences in each row, column, and box
        rows  = defaultdict(set)
        cols  = defaultdict(set)
        boxes = defaultdict(set)

        # Check for duplicates, iterating over each item
        for i in range(len(board)):
            for j in range(len(board)):
                x = board[i][j]

                if x == '.': continue
                if (x in rows[i] or
                    x in cols[j] or
                    x in boxes[i // 3, j // 3]):
                    return False

                rows[i].add(x)
                cols[j].add(x)
                boxes[i // 3, j // 3].add(x)

        return True
