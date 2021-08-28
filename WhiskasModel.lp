\* The_Whiskas_Problem *\
Minimize
Total_Cost_of_Ingredients_per_can: 0.008 BeefPercent + 0.013 ChickenPercent
 + 0.001 GelPercent + 0.01 MuttonPercent + 0.002 RicePercent
 + 0.005 WheatPercent
Subject To
FatRequirement: 0.1 BeefPercent + 0.08 ChickenPercent + 0.11 MuttonPercent
 + 0.01 RicePercent + 0.01 WheatPercent >= 6
FibreRequirement: 0.005 BeefPercent + 0.001 ChickenPercent
 + 0.003 MuttonPercent + 0.1 RicePercent + 0.15 WheatPercent <= 2
PercentagesSum: BeefPercent + ChickenPercent + GelPercent + MuttonPercent
 + RicePercent + WheatPercent = 100
ProteinRequirement: 0.2 BeefPercent + 0.1 ChickenPercent + 0.15 MuttonPercent
 + 0.04 WheatPercent >= 8
SaltRequirement: 0.005 BeefPercent + 0.002 ChickenPercent
 + 0.007 MuttonPercent + 0.002 RicePercent + 0.008 WheatPercent <= 0.4
Bounds
 0 <= ChickenPercent
Generals
ChickenPercent
End
