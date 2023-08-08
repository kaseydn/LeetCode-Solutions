class Solution:
    def carFleet(self, target, position, speed):
      #Models a stack
      lane = []
      #Sort by positions, cars represented by tuple = (position, speed)
      for pos, spd in sorted(zip(position, speed))[::-1]:
         #If lane is empty add the car
         if not len(lane):
            lane.append((pos, spd))
         #Otherwise you are comparing the current car's trajectory to the leading car
         else:
            lead_pos, lead_spd = lane[-1]
            #If the current car is projected to get there slower, it becomes it's own fleet
            if (target - pos) / spd > (target - lead_pos) / lead_spd:
               lane.append((pos, spd))
      #The answer will consist of the length of the stack
      return len(lane)
            
soln = Solution()
print(soln.carFleet(12, position=[10,8,0,5,3], speed=[2,4,1,1,3]))


