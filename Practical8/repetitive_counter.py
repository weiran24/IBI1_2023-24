import re
seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
pattern=r'(GTGTGT|GTCTGT)'
total=0
count=r'(?=('+ pattern + r'))'
matches= re.finditer(count,seq)
total=sum(1 for _ in matches)
print(total) 
