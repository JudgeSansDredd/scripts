import random
import matplotlib.pyplot as plt

NUM_TARGET=12
NUM_CARDS=99
NUM_NON_TARGET=NUM_CARDS-NUM_TARGET
NUM_ATTEMPTS=1_000_000
NUM_CARDS_SEEN=35

def make_deck():
    deck = ['target'] * NUM_TARGET + ['non_target'] * NUM_NON_TARGET
    return deck

def plot_histogram(results):
    labels = list(results.keys())
    counts = list(results.values())

    plt.bar(labels, counts)
    plt.xlabel('Number of Targets Drawn')
    plt.ylabel('Frequency (%)')
    plt.title('Histogram of Targets in Hand')
    plt.show()

def print_results(results):
    for key, value in results.items():
        print(f'{key} target(s): {value / NUM_ATTEMPTS * 100:.2f}%')

def order_results(results):
    keys = [str(i) for i in sorted([int(key) for key in results.keys()])]
    ordered_results = {}
    for key in keys:
        ordered_results[key] = results[key]
    return ordered_results


def main():
    results = {}
    for _ in range(NUM_ATTEMPTS):
        deck = make_deck()
        random.shuffle(deck)
        hand = deck[:NUM_CARDS_SEEN]
        num_targets = hand.count('target')
        if str(num_targets) in results:
            results[str(num_targets)] += 1
        else:
            results[str(num_targets)] = 1
    ordered_results = order_results(results)
    print_results(ordered_results)
    plot_histogram(ordered_results)


if __name__ == '__main__':
    main()