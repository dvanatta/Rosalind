import unittest
import dna 
#maybe roll this into a parser test?
#include parser test on simple files for both txt and rosalind

dataset = parser.parse_rosalind("ex5.txt")

class DNATests(unittest.TestCase):


    def test_counting_nucs(self):
        self.assertEqual((20, 12, 17, 21), dna.count('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'))
 

    def test_rna_sense(self):
        self.assertEqual('GAUGGAACUUGACUACGUAAAUU', dna.to_rna_sense('GATGGAACTTGACTACGTAAATT'))


    def test_dna_rev_comp(self):
        self.assertEqual('ACCGGGTTTT', dna.rev_comp('AAAACCCGGT', "dna"))


    def test_rna_rev_comp(self):
        self.assertEqual('ACCGGGUUUU',dna.rev_comp('AAAACCCGGT', "rna"))

#    def test_gc(self):
#        self.assertAlmostEqual('Rosalind_6404'

if __name__ == '__main__':
    unittest.main()
