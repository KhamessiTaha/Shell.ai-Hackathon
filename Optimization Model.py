import pulp as lp
import pandas as pd
demand = pd.read_csv('./dataset/demand.csv')
vehicles = pd.read_csv('./dataset/vehicles.csv')
vehicles_fuels = pd.read_csv('./dataset/vehicles_fuels.csv')
fuels = pd.read_csv('./dataset/fuels.csv')
carbon_emissions = pd.read_csv('./dataset/carbon_emissions.csv')
sample_submission = pd.read_csv('./dataset/sample_submission.csv')



prob = lp.LpProblem("Fleet_Optimization", lp.LpMinimize)

