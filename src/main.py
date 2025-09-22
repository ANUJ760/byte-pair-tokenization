import argparse
from tokenizer import BPE

def main():
    parser = argparse.ArgumentParser(description="Minimal BPE Tokenizer")
    parser.add_argument("--corpus", type=str, default="../alice.txt", help="Path to input file")
    parser.add_argument("--merges", type=int, default=50, help="number of merges")
    parser.add_argument("--encode", type=str, help="text to encode")
    parser.add_argument("--decode", nargs='+', type=int, help="pids to decode")
    parser.add_argument("--save", action="store_true", help="save output to output.txt")
    args = parser.parse_args()

    with open(args.corpus, "r", encoding="utf-8") as f:
        corpus = f.read()

    tokenizer = BPE()
    tokenizer.train(corpus, args.merges)

    outputs = []

    if args.encode:
        tokens, ids = tokenizer.encode_sentence(args.encode)
        outputs.append(f"Encoded tokens: {tokens}")
        outputs.append(f"Encoded ids: {ids}")

    if args.decode:
        text = tokenizer.decode(args.decode)
        outputs.append(f"Decoded text: {text}")

    result = "\n".join(outputs)
    print(result)

    if args.save:
        with open("../output.txt", "w", encoding="utf-8") as f:
            f.write(result)

if __name__ == "__main__":
    main()
