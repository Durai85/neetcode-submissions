class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0: return False

        unique = set(hand)
        count = Counter(hand)

        for card in sorted(unique):
            needed = count[card]
            print(card,needed)
            if needed > 0:
                for k in range(groupSize):
                    if card + k not in count or count[card + k] < needed:
                        return False
                    count[card + k] -= needed

        return True