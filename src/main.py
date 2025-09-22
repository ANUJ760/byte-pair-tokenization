import argparse
from tokenizer import BPE  # Assuming your class is in BPE.py

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train and encode with BPE")
    parser.add_argument("file", type=str, help="Path to the text file")
    parser.add_argument("--max_vocab", type=int, default=50, help="Maximum merges for BPE")
    parser.add_argument("--encode", type=str, default=None, help="Sentence to encode (optional)")
    args = parser.parse_args()
    
    with open(args.file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    bpe = BPE()
    bpe.train(text, max_vocab_size=args.max_vocab)
    
    if args.encode:
        tokens, ids = bpe.encode_sentence(args.encode)
        print("Encoded tokens:", tokens)
        print("Encoded IDs:", ids)
        decoded = bpe.decode(ids)
        print("Decoded sentence:", decoded)
