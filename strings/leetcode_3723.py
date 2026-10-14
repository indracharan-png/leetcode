class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        max_value = num * 9
        # Edge case - See if the desired sum is possible 
        if sum > max_value:
            return ""
        
        output = ""

        while sum > 9:
            output += '9'
            sum -= 9

        output += str(sum)

        trailing_spaces = num - len(output)

        if trailing_spaces > 0:
            output += ("0" * trailing_spaces)

        return output

