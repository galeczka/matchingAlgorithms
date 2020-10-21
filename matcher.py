import argparse
import string


def partial_match_table(pattern):
    """Creates partial match table from pattern."""
    T = {}
    T[0] = -1
    i = -1
    for q in range(1, len(pattern)):
        while i > -1 and pattern[i + 1] != pattern[q]:
            i = T[i]
        if pattern[i + 1] == pattern[q]:
            i += 1
        T[q] = i
    return T

def kmp(text, pattern):
    """Returns starting positions of pattern occurences."""
    T = partial_match_table(pattern)
    q = 0
    result = []
    for i in range(len(text)):
        while q > 0 and pattern[q] != text[i]:
            q = T[q - 1] + 1
        if pattern[q] == text[i]:
            q += 1
        if q == len(pattern):
            shift = i - len(pattern) + 1
            result.append(shift)
            q = T[q - 1] + 1
    return result

def transition_function(pattern):
    """Creates the transition function."""
    TF = {}
    for q in range(len(pattern) + 1):
        for char in string.printable:
            i = min(len(pattern) + 1, q + 2) - 1
            while not (pattern[:q] + char).endswith(pattern[:i]):
                i -= 1
            TF[(q, char)] = i
    return TF

def finite_automaton(text, pattern):
    """Returns starting positions of pattern occurences."""
    TF = transition_function(pattern)
    result = []
    q = 0
    pattern_length = len(pattern)
    for i, t in enumerate(text):
        q = TF[(q, t)]
        if q == pattern_length:
            shift = i - pattern_length + 1
            result.append(shift)
    return result


def main():
    parser = argparse.ArgumentParser(
        description='Presentation of pattern matching algorithms'
        )
    parser.add_argument(
        'type', type=str, choices=['KMP', 'FA'],
        help='type of algorithm: KMP - Knuth-Morris-Pratt, FA - finite automation'
        )
    parser.add_argument('text', type=str)
    parser.add_argument('pattern', type=str)       
    args = parser.parse_args()

    if args.type == 'KMP':
        print(kmp(args.text, args.pattern))
    else:
        print(finite_automaton(args.text, args.pattern))

main()
