def rowcol(matrix, rowstart, colstart, base, poss, doneflag):
	for i in range(colstart,4):
		for j in range(rowstart,4):
			if(i == 3 and j == 3):
				doneflag = True
			if(matrix[i][j] == 0):
				for k in range(base,5):
					if(k != matrix[i][0] and k != matrix[i][1] and k != matrix[i][2] and k != matrix[i][3]):
						if(k != matrix[0][j] and k != matrix[1][j] and k != matrix[2][j] and k != matrix[3][j]):
							if(i <= 1 and j <= 1):
								if(k != matrix[0][0] or k != matrix[0][1] or k != matrix[1][0] or k != matrix[1][1]):
									matrix[i][j] = k
									return True
							if(i <= 1 and j >= 2):
								if(k != matrix[0][2] or k != matrix[0][3] or k != matrix[1][2] or k != matrix[1][3]):
									matrix[i][j] = k
									return True
							if(i >= 2 and j >= 2):
								if(k != matrix[2][2] or k != matrix[2][3] or k != matrix[3][2] or k != matrix[3][3]):
									matrix[i][j] = k
									return True
							if(i >= 2 and j <= 1):
								if(k != matrix[2][0] or k != matrix[3][0] or k != matrix[2][1] or k != matrix[3][1]):
									matrix[i][j] = k
									return True
				if(doneflag == True):
					return False
				else:
					rowstart = j
					colstart = i
					if(rowstart == 0):
						rowstart = 3
						colstart = i-1
						base = matrix[colstart][rowstart]
					else:
						rowstart = j-1
						while(poss[colstart][rowstart] == 0):
							if(rowstart != 0):
								rowstart = rowstart-1
							else:
								colstart = i-1
								rowstart = 3
						base = matrix[colstart][rowstart]
						base = base+1
						matrix[colstart][rowstart] = 0
					rowcol(matrix, rowstart, colstart, base, poss, doneflag)
					return True
def main():
	w, h = 4, 4
	rowstart = 0
	colstart = 0
	base = 1
	case = True
	doneflag = False
	poss = [[0 for p in range(w)] for o in range(h)]
	matrix = [[0 for x in range(w)] for y in range(h)]	
	for i in range(0,4):
		value = input()
		matrix[i][0] = value[0]
		matrix[i][1] = value[2]
		matrix[i][2] = value[4]
		matrix[i][3] = value[6]
		for j in range(0,4):
			if(matrix[i][j] == "x"):
				matrix[i][j] = 0
				poss[i][j] = 1
			else:
				matrix[i][j] = int(matrix[i][j])
				poss[i][j] = 0



	while(case == True):
		case = rowcol(matrix, rowstart, colstart, base, poss, doneflag)

	for i in range(0,4):
		print()
		for j in range(0,4):
			print(matrix[i][j], end=" ")

main()
