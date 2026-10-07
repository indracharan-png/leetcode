class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        output_li = []
        curr_li = [] # This list keeps track of elements added from recursive function

        def backtrack(curr_idx: int, curr_target: int, candidates: list[int]) -> None:
            # Base cases
            if curr_target == 0:
                output_li.append(curr_li.copy())
                return
            if curr_target < 0 or curr_idx >= len(candidates):
                return

            # Choice-1: Do not consider the candidate element at current index
            backtrack(curr_idx + 1, curr_target, candidates)

            # Choice-2: Consider the candidate element at current index (allow reuse)
            curr_li.append(candidates[curr_idx])
            backtrack(curr_idx, curr_target - candidates[curr_idx], candidates)
            # Backtrack step, restore the previous instance of current list
            curr_li.pop()

        backtrack(0, target, candidates)
        return output_li

                
                

        