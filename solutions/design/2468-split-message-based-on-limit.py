class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        # Take Length of String, check if coverable by single digits, then by triple digits...
        def findMaxSplits(order, limit):
            splits = 0
            total_need = len(message)
            base = 5 + order - 1
            for i in range(order):
                if 9 * (10**i) * (limit - (base+i)) < total_need:
                    total_need -= 9 * (10**i) * (limit - (base+i))
                    splits += 9 * (10**i)

                else:
                    splits += math.ceil(total_need/(limit - (base+i)))

            return splits


        def max_characters(limit):
            base = 5
            order = 1
            while limit > (base+order-1):
                total = 0
                for i in range(order):
                    total += 9 * (10**i) * (limit - (base+i))

                if total >= len(message):
                    return order
                base += 1
                order += 1
            return -1

        max_order = max_characters(limit)
        if max_order == -1:
            return []

        max_splits = findMaxSplits(max_order, limit)
        covered = len(message)
        current_split = 1
        result = []
        left = 0
        while current_split <= max_splits:
            split_length = 3 + max_order + len(str(current_split))
            text_length = limit-split_length
            result.append(f"{message[left:left+text_length]}<{current_split}/{max_splits}>")
            
            left += text_length
            current_split += 1
            covered -= text_length

        return result


