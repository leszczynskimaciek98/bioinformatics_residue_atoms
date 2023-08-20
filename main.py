import py3Dmol as py3Dmol
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.PDB import PDBParser, MMCIFParser

pdb_format = "C:/Users/48512/Desktop/6lu7.pdb"

parser = PDBParser()

structure = parser.get_structure("6LU7",pdb_format)
#print(len(structure))
model = structure[0]

for chain in model:
    print(f'Chain {chain}, Chain_ID{chain.id}')
    for residue in chain:
        for atom in residue:
            print(atom)
