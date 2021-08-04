class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        index = -1
        
        gc = []
        for i in range(len(gas)):
            gc.append(gas[i]-cost[i])
        
        for i in range(len(gc)):
            gas_cost = gc[i:] + gc[:i]
            # print(gas_cost)
            tank = 0
            for j in range(len(gas_cost)):
                tank += gas_cost[j]
                # print('---', tank)
                if tank < 0:
                    break
            else:
                index = i
                
        return index