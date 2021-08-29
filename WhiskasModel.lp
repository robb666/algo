\* The_Whiskas_Problem *\
Minimize
Total_Cost_of_Ingredients_per_can: 0.008 Ingri_BEEF + 0.013 Ingri_CHICKEN
 + 0.001 Ingri_GEL + 0.01 Ingri_MUTTON + 0.002 Ingri_RICE + 0.005 Ingri_WHEAT
Subject To
FatRequirement: 0.1 Ingri_BEEF + 0.08 Ingri_CHICKEN + 0.11 Ingri_MUTTON
 + 0.01 Ingri_RICE + 0.01 Ingri_WHEAT >= 6
FibreRequirement: 0.005 Ingri_BEEF + 0.001 Ingri_CHICKEN + 0.003 Ingri_MUTTON
 + 0.1 Ingri_RICE + 0.15 Ingri_WHEAT <= 2
PercentagesSum: Ingri_BEEF + Ingri_CHICKEN + Ingri_GEL + Ingri_MUTTON
 + Ingri_RICE + Ingri_WHEAT = 100
ProteinRequirement: 0.2 Ingri_BEEF + 0.1 Ingri_CHICKEN + 0.15 Ingri_MUTTON
 + 0.04 Ingri_WHEAT >= 8
SaltRequirement: 0.005 Ingri_BEEF + 0.002 Ingri_CHICKEN + 0.007 Ingri_MUTTON
 + 0.002 Ingri_RICE + 0.008 Ingri_WHEAT <= 0.4
End
