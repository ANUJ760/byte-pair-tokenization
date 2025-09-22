# A minimal implementation of BPE algorithm for subword tokenization

from collections import Counter

class BPE:
    def __init__(self): # Initializes the BPE object (constructor method)
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
    
    def merge_pairs(self, pair, vocab):
        merged_pair = {}
        x, y = pair
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
            merged_pair[tuple(new_symb)] = merged_pair.get(tuple(new_symb), 0) + freq # Adds the frequency of the merged word to the dictionary
        return merged_pair 
    
    def train(self, sentences, max_vocab_size=30):
        vocab = self.build_vocab(sentences)
        self.merges = [] # Stores the merged pairs during training
        for _ in range(max_vocab_size):
            pairs = self.get_attrributes(vocab)
            if not pairs: # If no more pairs can be merged, break the loop
                break
            best = max(pairs, key=pairs.get) # Finds the pair with the highest frequency (most common pair)
            self.merges.append(best) # Adds the best pair to the list of merged pairs
            vocab = self.merge_pairs(best, vocab) # Merges the most common pair in the vocabulary
            
        token = set() # Stores the unique tokens
        for symbol in vocab.keys():
            token.update(symbol) # Adds the unique symbols in the vocabulary to the set of tokens
        print(token)  
        self.token2id = {token: idx for idx, token in enumerate(sorted(token))} # Converts the set of tokens to a dictionary of token IDs
        self.id2token = {idx: token for idx, token in self.token2id.items()} # Converts the set of ids to a dictionary of token strings
        
    
    def EncodeWords(self, word):
        symb = tuple(list(word) + ['</w>'])  # Adds an "end of the word" token '</w>' at the end of each word
        for pair in self.merge:
            i = 0
            while i < len(symb) - 1:
                if symb[i] == pair[0] and symb[i+1] == pair[1]:
                    symb[i] = symb[i] + symb[i+1]   # If the pair is found, merge them
                    del symb[i+1] # Removes the second symbol from the word as it has been merged
                else:
                    i += 1 # If the pair is not found, move to the next symbol in the word
        return symb
    def encode_sentence(self, sentences):
        tokens, ids = [], [] # Stores the list of tokens and their IDs respectively
        for word in sentences.split():
            s = self.EncodeWords(word) # Encodes each word
            tokens.extend(s) # Adds the encoded words to the list of tokens
            ids.extend([self.token2id[t] for t in s]) # Adds the token IDs of the encoded words to the list of IDs
        return tokens, ids
    
    def decode(self, ids):
        output, current = [], '' # Stores the decoded tokens and the current token being decoded
        for idx in ids:
            t = self.id2token[idx]
            if t.endswith('</w>'):
                current += t[:-4] # Removes the "end of the word" token '</w>' from the current token, as it has been decoded
                output.append(current)
                current = '' # Resets the current token so that the next decoded token starts from an empty word
            else:
                current += t # Adds the current character to the current token if it is not the end of the word token
                
        if current: # If there is any remaining token that hasn't been decoded, add it to the output
            output.append(current)
        print(' '.join(output)) # Prints the decoded tokens sentence-wise
        return ' '.join(output) # Joins the tokens to form a sentence
            
    # This function can be used to test the minimal BPE implementation.