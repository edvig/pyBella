from Bio.Seq import Seq
Fita1 = Seq("AAGCTGACTGGC")
print("Primeira fita", Fita1)
Fita2 = Fita1.complement()
print ("Fita complementar", Fita2)
print("---")
RNAFita1 = Fita1.complement_rna()
print("RNA da primeita fita", RNAFita1)
RNAFita2 = RNAFita1.complement_rna()
print ("RNA da fita complementar",RNAFita2)
print("---")
CodãoInicialFita1 = (Fita1[0:3])
print ("Codão inicial da primeira fita",CodãoInicialFita1)
CodãoComplementar1 = CodãoInicialFita1.complement()
print ("Codão complementar da primeira fita", CodãoComplementar1)
print ("ou")
CodãoComplementar2 = (Fita2[0:3])
print ("Codão complementar da primeira fita", CodãoComplementar2)
print ("---")

from Bio.SeqUtils import GC


