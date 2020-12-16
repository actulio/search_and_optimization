from scipy import stats
import scikit_posthocs as sp
import matplotlib.pyplot as plt
import pandas as pd

import statistics


# hillclimbing, simulated annealing, tabu, mi plus lambda, ga with elitism, pso

sphere = [
  [-449.08, -448.84, -448.93, -448.81, -448.61, -448.74, -448.85, -448.65, -448.92, -448.69],
  [-448.32, -447.73, -447.36, -448.65, -448.15, -447.16, -448.42, -448.23, -448.45, -448.89],
  # [-448.32, -447.73, -447.36, -448.65, -448.15, -447.16, -448.42, -448.23, -448.45, -448.8], # TABU
  [-449.04, -449.02, -449.04, -449.02, -449.18, -449.05, -449.08, -449.13, -449.17, -449.18],
  [-448.4, -448.93, -448.61, -448.59, -448.9, -448.79, -448.99, -449.05, -448.58, -448.62]
]

rosenbrock = [
  [743.46, 743.51, 2603.57, 639.54, 868.75, 727.73, 700.74, 608.72, 1313.97, 614.04],
  [3860.04, 8372.71, 859.85, 4729.75, 1151.68, 848.69, 752.76, 827.4, 9869.73, 696.36],
  # [965.78, 6554.15, 914.4, 1304.8, 773.12, 1045.78, 880.27, 911.54, 9405.24, 866.11], # TABU
  [755.6, 628.42, 549.94, 707.82, 610.78, 613.6, 576.17, 589.9, 561.14, 665.49],
  [640.14, 648.05, 645.24, 653.75, 7495.22, 665.0, 1430.99, 661.11, 686.82, 949.31]
]

rastringin = [
  [-327.51, -327.02, -326.12, -328.04, -326.95, -327.99, -327.5, -326.59, -327.11, -327.51],
  [-327.61, -326.84, -325.25, -327.43, -327.29, -326.68, -328.35, -325.94, -328.13, -326.13],
  # [-328.51, -328.47, -328.62, -328.67, -327.46, -328.51, -327.47, -328.34, -328.25, -327.97],
  [-113.89, -99.715, -127.23, -166.96, -130.43, -195.51, -177.75, -132.39, -174.43, -95.645],
  [174.75, 65.569, 88.320, 30.607, 135.21, 200.41, 152.79, 34.273, 33.141, 133.35],
]

ackley = [
  [
    -139.73160270715067,
    -139.780980651682,
    -139.7946815269327,
    -139.7990950584239,
    -139.74388421828462,
    -139.6807463381419,
    -139.76438869133358,
    -139.74401434518873,
    -139.7570566123419,
    -139.77704607152953,
  ],
  [
    -139.72191028411657,
    -139.6518323381397,
    -139.71976046950746,
    -139.65460434553952,
    -139.56805262211094,
    -139.45300783923744,
    -139.6582659486295,
    -139.77369706171427,
    -139.67095788326424,
    -139.7084089320813,
  ],
  [
    -138.75965298675737,
    -138.95122077666144,
    -131.8384782184929,
    -126.88977624090695,
    -138.78218374339068,
    -138.7665255128671,
    -126.55749957636813,
    -120.44651809100648,
    -138.73424304597998,
    -138.7554493748988,
  ],
  [
    -135.87105636736493,
    -137.1845589010984,
    -136.4193646687643,
    -136.38280418045684,
    -136.04564057883232,
    -131.95384447886647,
    -135.44932248149559,
    -134.5512343963325,
    -134.85503527438235,
    -134.46203270315036,
  ],
]


# df = pd.DataFrame(rastringin).T
# df.to_excel(excel_writer = "C:/Users/Tulio/Desktop/Mestrado/Busca_e_Otimizacao/search_and_optmization/src/utils/test.xlsx")


data = ackley

print(statistics.pstdev(data[2]))

# Friedman de grupo
print(stats.friedmanchisquare(*data))

# Kruskal-Wallis de grupo
print(stats.kruskal(*data))

#Teste de Conover baseado em Kruskal-Wallis
pc = sp.posthoc_conover(data)

#Caso precise mudar os indices e colunas do DataFrame
pc.columns = ['HC', 'SA', 'GA Elitism', 'PSO']
pc.index = ['HC', 'SA', 'GA Elitism', 'PSO']

print(pc)

#Heatmap do Teste de Conover
cmap = ['1', '#fb6a4a',  '#08306b',  '#4292c6', '#c6dbef']
heatmap_args = {'cmap': cmap, 'linewidths': 0.25, 'linecolor': '0.5', 'clip_on': False, 'square': True, 'cbar_ax_bbox': [0.80, 0.35, 0.04, 0.3]}
sp.sign_plot(pc, **heatmap_args)
plt.show()

#Exportar Dataframe para Latex
print(pc.to_latex(decimal=",", float_format="%.2f"))