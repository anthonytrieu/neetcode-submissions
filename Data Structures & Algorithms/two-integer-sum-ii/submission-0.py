class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers
        index1 = 0
        index2 = len(numbers) - 1
        result = []

        # 
        while index1 < index2:
            if numbers[index1] + numbers[index2] == target:
                result.append(index1 + 1)
                result.append(index2 + 1)

                return result
            elif numbers[index1] + numbers[index2] < target:
                index1 += 1
            else:
                index2 -= 1
            




            
            # depends on the target number
            # which index we shift
            # meaning that we increment either
            # index1 or 2 depending on
            # what we have for the target