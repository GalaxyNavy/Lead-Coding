class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

 below commented line consumes more execution time hence using hashmap is best 

       # n = nums

        # for i in  range(len(nums)):
        #     number = target - n[i]
        #     adding= n[i]


        #     n.remove(n[i])
        #     print(n)
        #     n.insert(i,-1.5)
        #     print(n)
        #     if number in n:
        #         # print(n)
        #         result.append(i)
        #         result.append(n.index(number))
        #         print(result)
        #         break


        #     else: 
        #         n.remove(-1.5)
        #         n.insert(i, adding


        hash_map = {}
        for i, val in enumerate(nums)  :
            remain = target-val

            if remain  in hash_map :
                return (hash_map[remain], i  )

            hash_map[val] =  i        

        return 
