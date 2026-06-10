class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        sk = []
        for t in asteroids:
            while(sk and sk[-1]>0 and t<0):
                if sk[-1] < -t :
                    sk.pop()
                elif sk[-1] == -t :
                    sk.pop()
                    break
                else:
                    break
            else: 
                sk.append(t)
        return sk