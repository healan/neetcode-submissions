import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntDic = {}
        heap = []
        rslt = []
        for num in nums:
            if num not in cntDic:
                cntDic[num] = 1
            else:
                cntDic[num] += 1
        
        heap = [(-cnt, num) for num, cnt in cntDic.items()]
        heapq.heapify(heap)
        
        for i in range(k):
            count, num = heapq.heappop(heap)
            rslt.append(num)
        
        return rslt

        
        