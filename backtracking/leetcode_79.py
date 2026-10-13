class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
       m, n = len(board), len(board[0])
       # To keep track of previously visited cells
       visited = [[-1 for _ in range(n)] for _ in range(m)]
       four_dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

       def search(curr_i, curr_j, word_idx, visited, board, word) -> bool:

          # Base-case: Character mismatch
           if board[curr_i][curr_j] != word[word_idx]:
               return False

           # Base-case: Reachex end of word. Found out the word
           if word_idx == len(word) - 1:
               return True
          
           # Mark the current cell visited
           visited[curr_i][curr_j] = 1

           # Explore all four neighbouring cells of current cell
           for x, y in four_dir:
               new_i, new_j = curr_i + x, curr_j + y
               # Ignore out of bounds indices of matrix
               if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                  continue
               # Skip over already visited cell
               if visited[new_i][new_j] == 1:
                   continue
               output = search(new_i, new_j, word_idx + 1, visited, board, word)
               if output: return True

           # Backtrack step: Restore the older instance
           visited[curr_i][curr_j] = -1

           return False


       for i in range(m):
           for j in range(n):
               output = search(i, j, 0, visited, board, word)
               if output: return True

       return False
               
               
               




        
            

        