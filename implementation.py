import numpy as np
# input of sequences
seq1 = "ACGATACG"
seq2 = "TACGTCG"

# scoring metrics
match_score = 1
mismatch_score = -1
gap_score = -2

# Need to build (1) scoring matrix and (2) traceback matrix
# Scoring matrix: stores scores for local alignments
# Traceback matrix: provides information for how the scores were computed


# INITIALIZING:

# 1) Matrices
#np.zeros(rows, columns)
scoring_matrix = np.zeros((len(seq1) + 1, len(seq2) +1))
traceback_matrix = np.zeros((len(seq1) + 1, len(seq2) + 1), dtype=object)

# 2) Scores
# fill the first column or row with indices according to the length,
# then multiply by the gap score: 0, 1, 2, 3 ->  *-2 -> 0, -2, -4, -6
scoring_matrix[0,:] = np.arange(len(seq2) + 1) * gap_score
scoring_matrix[:,0] = np.arange(len(seq1) + 1) * gap_score

# 3) Traceback
traceback_matrix[0:,1:] = "H"
traceback_matrix[1:,0] = "V"


## DEFINING THE LOOP FOR SCORING AND TRACEBACK
for i in range(1, len(seq1) +1):
	for j in range(1, len(seq2) + 1):
		# Diagonal score
		if seq1[i-1] == seq2[j-1]:
			diag_score = scoring_matrix[i-1,j-1] + match_score
		else:
			diag_score = scoring_matrix[i-1,j-1] + mismatch_score
		# vertical score
		vert_score = scoring_matrix[i-1, j] + gap_score
		#horizontal
		horiz_score = scoring_matrix[i, j-1] + gap_score

		## CONDITIONS TO FILL SCORING AND TRACEBACK MATRICES
		best_score = max([diag_score, vert_score, horiz_score])
		direction = []
		if diag_score == best_score:
			direction.append("D")
			traceback_matrix[i,j] = ''.join(direction)
			scoring_matrix[i,j] = best_score
		if vert_score == best_score:
			direction.append("V")
			traceback_matrix[i,j] = ''.join(direction)
			scoring_matrix[i,j] = best_score
		if horiz_score == best_score:
			direction.append("H")
			traceback_matrix[i,j] = ''.join(direction)
			scoring_matrix[i,j] = best_score

print(traceback_matrix)
print(scoring_matrix)

