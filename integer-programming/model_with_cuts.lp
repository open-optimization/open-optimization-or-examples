\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  2 e[0,1] + 3 e[0,2] + 4 e[0,3] + 5 e[0,4] + 6 e[0,5] + 7 e[0,6] + 2 e[1,0]
   + 4 e[1,2] + 5 e[1,3] + 6 e[1,4] + 7 e[1,5] + 8 e[1,6] + 3 e[2,0]
   + 4 e[2,1] + 6 e[2,3] + 7 e[2,4] + 8 e[2,5] + 9 e[2,6] + 4 e[3,0]
   + 5 e[3,1] + 6 e[3,2] + 8 e[3,4] + 9 e[3,5] + 10 e[3,6] + 5 e[4,0]
   + 6 e[4,1] + 7 e[4,2] + 8 e[4,3] + 10 e[4,5] + 11 e[4,6] + 6 e[5,0]
   + 7 e[5,1] + 8 e[5,2] + 9 e[5,3] + 10 e[5,4] + 12 e[5,6] + 7 e[6,0]
   + 8 e[6,1] + 9 e[6,2] + 10 e[6,3] + 11 e[6,4] + 12 e[6,5]
Subject To
 R0: e[0,1] + e[0,2] + e[0,3] + e[0,4] + e[0,5] + e[0,6] = 1
 R1: e[1,0] + e[1,2] + e[1,3] + e[1,4] + e[1,5] + e[1,6] = 1
 R2: e[2,0] + e[2,1] + e[2,3] + e[2,4] + e[2,5] + e[2,6] = 1
 R3: e[3,0] + e[3,1] + e[3,2] + e[3,4] + e[3,5] + e[3,6] = 1
 R4: e[4,0] + e[4,1] + e[4,2] + e[4,3] + e[4,5] + e[4,6] = 1
 R5: e[5,0] + e[5,1] + e[5,2] + e[5,3] + e[5,4] + e[5,6] = 1
 R6: e[6,0] + e[6,1] + e[6,2] + e[6,3] + e[6,4] + e[6,5] = 1
 R7: e[1,0] + e[2,0] + e[3,0] + e[4,0] + e[5,0] + e[6,0] = 1
 R8: e[0,1] + e[2,1] + e[3,1] + e[4,1] + e[5,1] + e[6,1] = 1
 R9: e[0,2] + e[1,2] + e[3,2] + e[4,2] + e[5,2] + e[6,2] = 1
 R10: e[0,3] + e[1,3] + e[2,3] + e[4,3] + e[5,3] + e[6,3] = 1
 R11: e[0,4] + e[1,4] + e[2,4] + e[3,4] + e[5,4] + e[6,4] = 1
 R12: e[0,5] + e[1,5] + e[2,5] + e[3,5] + e[4,5] + e[6,5] = 1
 R13: e[0,6] + e[1,6] + e[2,6] + e[3,6] + e[4,6] + e[5,6] = 1
Bounds
Binaries
 e[0,1] e[0,2] e[0,3] e[0,4] e[0,5] e[0,6] e[1,0] e[1,2] e[1,3] e[1,4]
 e[1,5] e[1,6] e[2,0] e[2,1] e[2,3] e[2,4] e[2,5] e[2,6] e[3,0] e[3,1]
 e[3,2] e[3,4] e[3,5] e[3,6] e[4,0] e[4,1] e[4,2] e[4,3] e[4,5] e[4,6]
 e[5,0] e[5,1] e[5,2] e[5,3] e[5,4] e[5,6] e[6,0] e[6,1] e[6,2] e[6,3]
 e[6,4] e[6,5]
End
