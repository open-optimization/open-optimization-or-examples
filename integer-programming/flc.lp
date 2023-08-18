\ Model CapacitatedFacilityLocation
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  50 x[Center_1,Store_1] + 60 x[Center_1,Store_2] + 70 x[Center_1,Store_3]
   + 85 x[Center_1,Store_4] + 75 x[Center_2,Store_1]
   + 45 x[Center_2,Store_2] + 55 x[Center_2,Store_3]
   + 50 x[Center_2,Store_4] + 65 x[Center_3,Store_1]
   + 80 x[Center_3,Store_2] + 40 x[Center_3,Store_3]
   + 60 x[Center_3,Store_4] + 150000 y[Center_1] + 100000 y[Center_2]
   + 180000 y[Center_3]
Subject To
 StoreDemand_Store_1: x[Center_1,Store_1] + x[Center_2,Store_1]
   + x[Center_3,Store_1] = 1
 StoreDemand_Store_2: x[Center_1,Store_2] + x[Center_2,Store_2]
   + x[Center_3,Store_2] = 1
 StoreDemand_Store_3: x[Center_1,Store_3] + x[Center_2,Store_3]
   + x[Center_3,Store_3] = 1
 StoreDemand_Store_4: x[Center_1,Store_4] + x[Center_2,Store_4]
   + x[Center_3,Store_4] = 1
 CenterCapacity_Center_1: 40 x[Center_1,Store_1] + 30 x[Center_1,Store_2]
   + 20 x[Center_1,Store_3] + 25 x[Center_1,Store_4] - 100 y[Center_1]
   <= 0
 CenterCapacity_Center_2: 40 x[Center_2,Store_1] + 30 x[Center_2,Store_2]
   + 20 x[Center_2,Store_3] + 25 x[Center_2,Store_4] - 80 y[Center_2] <= 0
 CenterCapacity_Center_3: 40 x[Center_3,Store_1] + 30 x[Center_3,Store_2]
   + 20 x[Center_3,Store_3] + 25 x[Center_3,Store_4] - 90 y[Center_3] <= 0
Bounds
Binaries
 y[Center_1] y[Center_2] y[Center_3]
End
