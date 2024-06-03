import pulp as lp
import pandas as pd
#demand = pd.read_csv('./dataset/demand.csv')
#vehicles = pd.read_csv('./dataset/vehicles.csv')
#vehicles_fuels = pd.read_csv('./dataset/vehicles_fuels.csv')
#fuels = pd.read_csv('./dataset/fuels.csv')
#carbon_emissions = pd.read_csv('./dataset/carbon_emissions.csv')
sample_submission = pd.read_csv('./dataset/sample_submission.csv')
#vehicles_data = pd.read_csv('./dataset/vehicles_data.csv')
vehicles_all = pd.read_csv('./dataset/vehicles_all.csv')
demand_ce = pd.read_csv('./dataset/demand_ce.csv')
cost_profiles = pd.read_csv('./dataset/cost_profiles.csv')


years = [2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038]
#fuels = ['B20','BioLNG','Electricity','HVO','LNG']
# Si : x tons
Sizes = {'S1':17,'S2':44,'S3':50,'S4':64}
# Di : x km daily
Distances = {'D1':300,'D2':400,'D3':500,'D4':600}
# { end of year : ( resale , %ins , %mnt ) }
Yearly_cost = {1:(.9,5,1),
               2:(.8,6,3),
               3:(.7,7,5),
               4:(.6,8,7),
               5:(.5,9,9),
               6:(.4,10,11),
               7:(.3,11,13),
               8:(.3,12,15),
               9:(.3,13,17),
               10:(.3,14,19)}
#prob = lp.LpProblem("Fleet_Optimization", lp.LpMinimize)

#merged_df = pd.merge(vehicles, vehicles_fuels, on='ID')


#merged = pd.merge(demand, carbon_emissions, on='Year')
#merged.to_csv('./dataset/demand_ce.csv', index=False)