def unique_value_pairs(nums, target):
    """
    Return unique value pairs (no duplicate pair values). Each pair is (a, b) with a <= b.
    Uses each value only to check existence, but does not produce multiple identical pairs
    even if counts permit.
    """
    from collections import Counter
    cnt = Counter(nums)
    pairs = []
    for a in sorted(cnt):
        b = target - a
        if b < a:
            continue
        if b not in cnt:
            continue
        if a == b:
            if cnt[a] >= 2:
                pairs.append((a, a))
        else:
            pairs.append((a, b))
    return pairs


def max_disjoint_pairs(nums, target):
    """
    Return the maximum number of disjoint pairs (each element used at most once).
    Produces multiple identical-value pairs when counts permit (e.g., 4 fives -> two (5,5)).
    Pairs are returned as (a, b) with a <= b, sorted by a then b.
    """
    from collections import Counter
    cnt = Counter(nums)
    pairs = []
    for a in sorted(list(cnt.keys())):
        while cnt[a] > 0:
            b = target - a
            if b not in cnt or cnt[b] <= 0:
                break
            # ensure ordering a <= b and avoid double-handling when a > b
            if a > b:
                break
            if a == b:
                # how many (a,a) pairs can we make now
                k = cnt[a] // 2
                if k == 0:
                    break
                for _ in range(k):
                    pairs.append((a, a))
                cnt[a] -= 2 * k
                break
            else:
                # pair a with b, up to min(cnt[a], cnt[b])
                k = min(cnt[a], cnt[b])
                for _ in range(k):
                    pairs.append((a, b))
                cnt[a] -= k
                cnt[b] -= k
                break
    # sort pairs for deterministic order
    pairs.sort()
    return pairs


# default exported function (change to unique_value_pairs if you prefer that behavior)
def find_pairs(nums, target):
    """
    By default returns the maximum number of disjoint pairs.
    If you want only unique value pairs, replace the call below with unique_value_pairs(nums, target).
    """
    return max_disjoint_pairs(nums, target)


if __name__ == "__main__":
    # Provided test cases and what each implementation returns:
    tests = [
        ([2, 7, 11, 15, 3, 6], 9),
        ([1, 5, 3, 7, 2, 8], 10),
        ([1, 1, 1, 1], 2),
        ([5, 5, 5, 5], 10),
    ]

    print("Using find_pairs (max_disjoint_pairs):")
    for arr, t in tests:
        print(arr, t, "->", find_pairs(arr, t))

    print("\nUsing unique_value_pairs:")
    for arr, t in tests:
        print(arr, t, "->", unique_value_pairs(arr, t))