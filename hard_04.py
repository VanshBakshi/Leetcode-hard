class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # Each node stores:
        # prod = product of the whole segment modulo k
        # cnt[r] = number of non-empty prefixes with product % k == r
        tree = [None] * (4 * n)

        def merge(A, B):
            prodA, cntA = A
            prodB, cntB = B

            # Product of the combined segment
            prod = (prodA * prodB) % k

            cnt = [0] * k

            # Prefixes completely inside A
            for r in range(k):
                cnt[r] += cntA[r]

            # Prefixes containing all of A + a prefix of B
            for r in range(k):
                new_rem = (prodA * r) % k
                cnt[new_rem] += cntB[r]

            return (prod, cnt)

        def build(node, left, right):
            if left == right:
                rem = nums[left] % k

                cnt = [0] * k
                cnt[rem] = 1

                tree[node] = (rem, cnt)
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, left, right, pos, value):
            if left == right:
                rem = value % k

                cnt = [0] * k
                cnt[rem] = 1

                tree[node] = (rem, cnt)
                return

            mid = (left + right) // 2

            if pos <= mid:
                update(node * 2, left, mid, pos, value)
            else:
                update(node * 2 + 1, mid + 1, right, pos, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, left, right, ql, qr):
            # Complete overlap
            if ql <= left and right <= qr:
                return tree[node]

            mid = (left + right) // 2

            # Completely in left child
            if qr <= mid:
                return query(node * 2, left, mid, ql, qr)

            # Completely in right child
            if ql > mid:
                return query(node * 2 + 1, mid + 1, right, ql, qr)

            # Overlaps both children
            A = query(node * 2, left, mid, ql, qr)
            B = query(node * 2 + 1, mid + 1, right, ql, qr)

            return merge(A, B)

        # Build segment tree
        build(1, 0, n - 1)

        answer = []

        for index, value, start, x in queries:

            # Persistent update
            nums[index] = value
            update(1, 0, n - 1, index, value)

            # We need all non-empty prefixes of nums[start:]
            _, cnt = query(1, 0, n - 1, start, n - 1)

            answer.append(cnt[x])

        return answer
