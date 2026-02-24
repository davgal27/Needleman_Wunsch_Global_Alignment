# Needleman-Wunsch Global Alignment Algorithm

Aligns any two sequences using Needleman-Wunsch global alignment with custom match, mismatch, and gap scores. Finds all optimal alignments when multiple paths tie.

**Input:**  
- First sequence  
- Second sequence  
- Match score  
- Mismatch penalty  
- Gap penalty  

**Output:**  
- Scoring matrix  
- Traceback matrix  
- All optimal alignments (stacked)  
- Final alignment score