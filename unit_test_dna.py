import unittest
import dna
import dna_parser
# include parser test on simple files for both txt and rosalind

dataset = dna_parser.parse_rosalind("Examples/ex5.txt")
seq = dataset[0][1]

class DNATests(unittest.TestCase):


    def test_counting_nucs(self):
        self.assertEqual((20, 12, 17, 21), dna.count('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'))


    def test_rna_sense(self):
        self.assertEqual('GAUGGAACUUGACUACGUAAAUU', dna.to_rna_sense('GATGGAACTTGACTACGTAAATT'))


    def test_dna_rev_comp(self):
        self.assertEqual('ACCGGGTTTT', dna.rev_comp('AAAACCCGGT', "dna"))


    def test_rna_rev_comp(self):
        self.assertEqual('ACCGGGUUUU',dna.rev_comp('AAAACCCGGT', "rna"))


    def test_gc(self):
        self.assertAlmostEqual(.60919540, dna.calculate_gc("CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"),4)


    def test_hamming(self):
        self.assertEqual(7, dna.calculate_hamming('GAGCCTACTAACGGGAT','CATCGTAATGACGGCCT'))


    def test_translate(self):
        self.assertEqual("MAMAPRTEINSTRING", dna.translate("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"))


    def test_motif(self):
        self.assertEqual([2, 4, 10], dna.motif("GATATATGCATATACTT", "ATAT"))    
   
   
    def test_consensus(self):
        test_set = dna_parser.parse_fasta("Examples/ex_con.txt")
        con_seq, scores = dna.consensus(test_set)
        self.assertEqual("ATGCAACT", con_seq)
   
   
    def test_longest_common(self):
        pass


    def test_longest_dec_sub(self):
        self.assertEqual("0 2 6 9 11 15", dna.longest_subseq([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], "inc"))
        self.assertEqual("12 10 9 5 3", dna.longest_subseq([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], "dec"))


if __name__ == '__main__':
    unittest.main()
