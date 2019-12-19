
# 436ms/21.90%
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False

        hand.sort()
        for _ in range(len(hand) // W):
            minimum = hand[0]
            for num in range(minimum, minimum + W):
                try:
                    hand.remove(num)
                except ValueError:
                    return False

        return True