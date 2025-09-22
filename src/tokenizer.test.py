
def test_decode_empty_list(self):
    bpe = BPE()
    result = bpe.decode([])
    self.assertEqual(result, "")
