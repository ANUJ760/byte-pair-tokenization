from collections import Counter

class BPE:
    def __init__(self):
        self.id2token = {}
        self.token2id = {}
        self.merge = []
        
        
    def build_vocab(self, sentences):
        words = sentences.split( ) # Splits the sentences into words  (separates words by space)
        freq = Counter(words)
        vocab = {}
        for word, count in freq.items():
            symb = tuple(list(word) + ['</w>'])   # Adds an "end of the word" token '</w>' at the end of each word
            vocab[symb] = count # Stores the count of each symbolized word as a key value in the vocab dictionary
        return vocab
    
    def get_attributes(self, vocab):
        pairs = Counter() # Stores the frequency of each symbol pair
        for symbol, freq in vocab.items():
            for i in range(len(symbol) - 1):
                pair = (symbol[i], symbol[i+1])
                pairs[pair] += freq # Adds the frequency of the word (symbol) to each of the pairs in it
        return pairs
    
    def merge_pairs(self, pairs, vocab):
        merged_pairs = {}
        x, y = pairs
        for symbol, freq in vocab.items():
            new_symb = []
            i = 0
            while i < len(symbol) - 1:
                if i < len(symbol) - 1 and (symbol[i], symbol[i+1]) == (x, y):
                    new_symb.append(symbol[i] + symbol[i+1])   # If the pair is found, merge them
                    i += 2
                else:
                    new_symb.append(symbol[i])  # If the pair is not found, add the symbol as it is
                    i += 1
            merged_pairs[tuple(new_symb)] = merged_pairs.get(tuple(new_symb), 0) + freq # Adds the frequency of the merged word to the dictionary
        return merged_pairs 
    
    def train(self, sentences, max_vocab_size=30):
        vocab = self.build_vocab(sentences)
        self.merges = [] # Stores the merged pairs during training
        for _ in range(max_vocab_size):
            pairs = self.get_attrributes(vocab)
            if not pairs:
                break
            best = max(pairs, key=pairs.get) # Finds the pair with the highest frequency (most common pair)
            self.merges.append(best) # Adds the best pair to the list of merged pairs
            vocab = self.merge_pairs(best, vocab) # Merges the most common pair in the vocabulary
    

            