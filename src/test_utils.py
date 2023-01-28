from collections import Counter

from matplotlib import pyplot as plt
from scipy.stats import entropy
from dahuffman import HuffmanCodec


def generate_histogram(input_data: bytes, plot_filepath: str):
    plt.hist(x=list(input_data), bins="auto",
             color="#0504aa", alpha=0.7, rwidth=0.85)
    plt.xlabel("Symbole")
    plt.ylabel("Ilość wystąpień")

    plt.savefig(plot_filepath)


def input_data_entropy(input_data: bytes) -> float:
    counted_symbols = Counter(list(input_data))
    total_symbol_count = sum(counted_symbols.values())
    probability_mass = {k: v/total_symbol_count for k,
                        v in counted_symbols.items()}

    return entropy(list(probability_mass.values()), base=2)


def average_bit_lenght(coder, input_data: bytes, encoded_data) -> float:
    if isinstance(coder, HuffmanCodec):
        number_of_bits = 0
        for element in input_data:
            number_of_bits += coder.get_code_table()[element][0]

        return number_of_bits / len(input_data)
    else:
        return len(encoded_data) / len(input_data)
