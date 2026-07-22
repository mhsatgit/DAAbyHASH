import random


def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    matches = []
    comparisons = 0

    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1

        if j == m:
            matches.append(i)

    return matches, comparisons


def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    return lps


def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)

    matches = []
    comparisons = 0
    i = j = 0

    while i < n:
        comparisons += 1

        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == m:
                matches.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparisons


def rabin_karp(text, pattern, q=101):
    n, m = len(text), len(pattern)
    d = 256
    h = pow(d, m - 1, q)

    p_hash = 0
    t_hash = 0
    matches = []
    comparisons = 0

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    for s in range(n - m + 1):
        if p_hash == t_hash:
            for k in range(m):
                comparisons += 1
                if text[s + k] != pattern[k]:
                    break
            else:
                matches.append(s)

        if s < n - m:
            t_hash = (
                d * (t_hash - ord(text[s]) * h) + ord(text[s + m])
            ) % q

            if t_hash < 0:
                t_hash += q

    return matches, comparisons


def main():
    text = "AABAACAADAABAABA"
    pattern = "AABA"

    print(f"Text: {text}")
    print(f"Pattern: {pattern}")

    naive_matches, naive_comp = naive_search(text, pattern)
    kmp_matches, kmp_comp = kmp_search(text, pattern)
    rk_matches, rk_comp = rabin_karp(text, pattern)

    print(f"\nNaive Search")
    print(f"Matches      : {naive_matches}")
    print(f"Comparisons  : {naive_comp}")

    print(f"\nKMP Search")
    print(f"Matches      : {kmp_matches}")
    print(f"Comparisons  : {kmp_comp}")

    print(f"\nRabin-Karp Search")
    print(f"Matches      : {rk_matches}")
    print(f"Comparisons  : {rk_comp}")

    text_large = "".join(random.choices("ABCD", k=10000))
    patterns = ["AB", "ABCD", "ABCDAB", "ABCDABCD"]

    print("\nPerformance Comparison")
    print(
        f'{"Pattern":<12} {"Naive":>12} {"KMP":>12} {"Rabin-Karp":>15}'
    )
    print("-" * 55)

    for p in patterns:
        _, naive_comp = naive_search(text_large, p)
        _, kmp_comp = kmp_search(text_large, p)
        _, rk_comp = rabin_karp(text_large, p)

        print(
            f"{p:<12} {naive_comp:>12} {kmp_comp:>12} {rk_comp:>15}"
        )


if __name__ == "__main__":
    main()