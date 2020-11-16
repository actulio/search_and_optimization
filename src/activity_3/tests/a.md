rastringin

hillclimbing

timer: 74689.759ms
Best combination of params: [
{ r: 1.1, p: 0.1, qval: 44.28150276738074 },
{ r: 1.4, p: 0.1, qval: -10.377071604443302 },
{ r: 1.3, p: 0.1, qval: -22.90546879170563 },
{ r: 2, p: 0.1, qval: -56.24696437314333 },
{ r: 1.2, p: 0.1, qval: -65.71343243856347 }
]
Best overall param: { r: 1.2, p: 0.1, qval: -65.71343243856347 }
Quality of chosen params: [
-1.7203794039132276,
-33.884546522944845,
1.076621787090346,
-40.69952358706331,
-51.715339236169825,
-0.6774793174090519,
-14.932813336271352,
-22.260887294521524,
0.39631429213301317,
-21.210920859069518
]

annealing

timer: 736975.471ms
Best combination of params: [
{ r: 2.8, p: 0.1, initialT: 1000, qval: -37.3680632624862 },
{ r: 1.2, p: 0.1, initialT: 5000, qval: -57.003040866657386 },
{ r: 2.3, p: 0.1, initialT: 10000, qval: -60.855647277221124 },
{ r: 2.2, p: 0.1, initialT: 1000, qval: -62.018122486769414 },
{ r: 1.2, p: 0.1, initialT: 3000, qval: -75.36462604177112 }
]
Best overall param: { r: 1.2, p: 0.1, initialT: 3000, qval: -75.36462604177112 }
Quality of chosen params: [
-73.74097922355895,
-15.906049499708956,
-32.90141076901074,
-41.29571337870044,
-19.955255060666047,
-42.65592819525892,
-23.030032456427648,
9.669378502081315,
-15.259224760914265,
-46.463396336393316
]

mi plus alpha

best combination of params: [
{ r: 2.4, p: 0.1, mi: 1, lambda: 8, qval: -45.76613164152906 },
{ r: 1.3, p: 0.1, mi: 1, lambda: 2, qval: -50.234992562331115 },
{ r: 2.4, p: 0.1, mi: 1, lambda: 2, qval: -50.47339629268686 },
{ r: 1.3, p: 0.1, mi: 1, lambda: 4, qval: -53.22765274078995 },
{ r: 1.2, p: 0.1, mi: 1, lambda: 1, qval: -64.57655619255092 }
]
Best overall param: { r: 1.2, p: 0.1, mi: 1, lambda: 1, qval: -64.57655619255092 }
Quality of chosen params: [
24.16496775761175,
29.262090085625687,
-55.411323412609136,
-13.38822986080038,
5.717711148879232,
44.70736217343671,
2.1865386367585984,
-19.18424139064018,
-15.068328345948487,
-33.37948948741001
]

# hill climbing

## rastringin

Best overall param: { r: 2.3, p: 0.1, qval: -43.433257451442614 }
Quality of chosen params: [
-21.857319308081628,
-17.636470779718422,
-15.653948628101034,
3.432644728732214,
-61.035336821157614,
7.265852157477809,
-7.103755825025303,
-63.7212368190784,
-23.81502408188544,
-64.58179566770627
]

# simulated annealing

## rastringin

Best overall param: { r: 2.3, p: 0.1, initialT: 1000, qval: -33.25063242587038 }
Quality of chosen params: [
-29.308054543014748,
8.609399494511763,
0.5035946809205711,
-38.78339254457353,
-20.204259827649196,
7.301687831074048,
-30.995316698536044,
-22.5322700385305,
-0.6774197847213372,
-42.05542840523299
]

# mi plus lambda

## sphere

-449.0491906620388
-449.02943193299143
-449.0440794114825
-449.02398127633376
-449.18581586249024
-449.05813584201644
-449.0819997666241
-449.1330339056138
-449.1788385667608
-449.1850351841663

mi = 1, lambda = 1, r = 0.5, p = 0.1 --- mi e lambda fazem pouca diferença aqui

## rosenbrock

755.6072072398986
628.4298417017802
549.9483670731667
707.8260439526166
610.7877325483275
613.6080191967567
576.1781787395244
589.9050108799628
561.1495405365586
665.4996768011262

{ mi: 1, lambda: 2 }, { r: 0.4, p: 0.1 },

## rastringin

-15.241692284387966
-33.44815881997323
-44.04853881789512
-14.565309557327453
-25.00722276591148
-61.184736886064
-2.207148206846796
-58.58435699772588
-15.011973814496912
-27.945862665122092

{ mi: 1, lambda: 2 }{ r: 1.2, p: 0.1 }

# ga with elistim

## sphere

-448.40735989216546
-448.9366624965503
-448.6129897609925
-448.59922610825794
-448.9061791019641
-448.7902132560861
-448.9959843055075
-449.05263569368674
-448.58918184700946
-448.6277505300695

{ popsize: 4, n: 2 } { r: 0.2, p: 0.1 }

## rosenbrock

640.1478956487014
648.0553884001904
645.2481260580062
653.7565313853033
7495.2208155617
665.0052956300221
1430.9902481243344
661.1192197657998
686.8291820583927
949.3160531268284

{ popsize: 6, n: 2 }, { r: 0.2, p: 0.1 }

## rastringin

217.22650680378354
188.59118078586266
273.40640318541966
192.9118246583305
301.7077429454861
187.1147900043228
230.78421451868405
257.33708814127453
223.7683490351318
175.9316684396128

{ popsize: 8, n: 1 } { r: 0.2, p: 0.1 }


{ popsize: 4, n: 2 },
{ r: 2, p: 0.01 },
[-113.89,-99.715,-127.23,-166.96,-130.43,-195.51,-177.75,-132.39,-174.43,-95.645];