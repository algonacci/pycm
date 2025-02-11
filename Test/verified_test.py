# -*- coding: utf-8 -*-
"""
>>> import numpy as np
>>> from pycm import *
>>> from pycm.pycm_overall_func import NIR_calc
>>> from pycm.pycm_ci import AUC_SE_calc,CI_calc
>>> NIR_calc({'Class2': 804, 'Class1': 196},1000) # Verified Case - (Caret package)
0.804
>>> cm = ConfusionMatrix([2, 0, 2, 2, 0, 1],[0, 0, 2, 2, 0, 2]) # Verified Case - (https://bit.ly/38nfMha)
>>> cm.print_matrix()
Predict 0       1       2
Actual
0       2       0       0
<BLANKLINE>
1       0       0       1
<BLANKLINE>
2       1       0       2
<BLANKLINE>
<BLANKLINE>
>>> cm = ConfusionMatrix(matrix={0:{0:3,1:1},1:{0:4,1:2}})   # Verified Case - (https://bit.ly/2DHQvjn)
>>> cm.LS[1]
1.1111111111111112
>>> cm.LS[0]
1.0714285714285714
>>> cm = ConfusionMatrix(matrix={"Class1":{"Class1":183,"Class2":13},"Class2":{"Class1":141,"Class2":663}})  # Verified Case - (Caret package)
>>> cm.PValue
0.000342386296143693
>>> cm = ConfusionMatrix(matrix={"Class1":{"Class1":4,"Class2":2},"Class2":{"Class1":2,"Class2":4}}) # Verified Case - (Delgado, Nunez-Gonzalez, 2018)
>>> cm.Overall_CEN
0.861654166907052
>>> cm.Overall_MCEN
0.6666666666666666
>>> cm.IS["Class1"]
0.4150374992788437
>>> cm.IS["Class2"]
0.4150374992788437
>>> cm = ConfusionMatrix(matrix={1:{1:5,2:0,3:0},2:{1:0,2:10,3:0},3:{1:0,2:300,3:0}})  # Verified Case - (Delgado, Nunez-Gonzalez, 2018)
>>> cm.Overall_CEN
0.022168905807495587
>>> cm.Overall_MCC
0.3012440235352457
>>> cm.CBA
0.3440860215053763
>>> cm = ConfusionMatrix(matrix={1:{1:1,2:3,3:0,4:0},2:{1:9,2:1,3:0,4:0},3:{1:0,2:0,3:100,4:0},4:{1:0,2:0,3:0,4:200}}) # Verified Case - (Branco et al., 2017)
>>> cm.RCI
0.9785616782831341
>>> cm = ConfusionMatrix(matrix={1:{1:1,2:0,3:3},2:{1:0,2:100,3:0},3:{1:0,2:0,3:200}}) # Verified Case - (Branco et al., 2017)
>>> cm.RCI
0.9264007150415143
>>> cm = ConfusionMatrix(matrix={1:{1:5,2:0,3:0},2:{1:0,2:10,3:0},3:{1:0,2:300,3:0}})  # Verified Case - (Branco et al., 2017)
>>> cm.RCI
0.3675708571923818
>>> cm = ConfusionMatrix(matrix={1:{1:12806,2:26332},2:{1:5484,2:299777}},transpose=True) # Verified Case - (Bekkar et al., 2013)
>>> cm.AUC[1]
0.8097090079101759
>>> cm.GI[1]
0.6194180158203517
>>> cm.Overall_ACC
0.9076187793808925
>>> cm.DP[1]
0.7854399677022138
>>> cm.Y[1]
0.6194180158203517
>>> cm.BM[1]
0.6194180158203517
>>> cm = ConfusionMatrix(matrix={1:{1:13182,2:30516},2:{1:5108,2:295593}},transpose=True) # Verified Case - (Bekkar et al., 2013)
>>> cm.AUC[1]
0.8135728157964055
>>> cm.GI[1]
0.627145631592811
>>> cm.Overall_ACC
0.896561836706843
>>> cm.DP[1]
0.770700985610517
>>> cm.Y[1]
0.627145631592811
>>> cm.BM[1]
0.627145631592811
>>> cm = ConfusionMatrix(matrix={1:{1:60,2:9,3:1,4:0,5:0,6:0},2:{1:23,2:48,3:0,4:2,5:2,6:1},3:{1:11,2:5,3:1,4:0,5:0,6:0},4:{1:0,2:2,3:0,4:7,5:1,6:3},5:{1:2,2:1,3:0,4:0,5:4,6:2},6:{1:1,2:2,3:0,4:2,5:1,6:23}}) # Verified Case - (https://bit.ly/2YdvM01)
>>> cm.AM[1]
27
>>> cm.BCD[1]
0.0630841121495327
>>> cm = ConfusionMatrix(matrix={1:{1:9,2:3,3:0},2:{1:3,2:5,3:1},3:{1:1,2:1,3:4}}) # Verified Case -- (https://bit.ly/2r80R9t)
>>> cm.CI95
(0.48885185570907297, 0.8444814776242603)
>>> cm.SE
0.09072184232530289
>>> cm.Overall_RACC
0.36625514403292175
>>> cm.Kappa
0.4740259740259741
>>> cm.KappaNoPrevalence
0.33333333333333326
>>> cm.KappaUnbiased
0.4734561213434452
>>> cm.ReferenceEntropy
1.5304930567574824
>>> cm.ResponseEntropy
1.486565953154142
>>> cm.CrossEntropy
1.5376219392005763
>>> cm.ConditionalEntropy
1.089255908674706
>>> cm.MutualInformation
0.39731004447943596
>>> cm.KL
0.007128882443093773
>>> cm.Chi_Squared
15.525641025641026
>>> cm.Phi_Squared
0.5750237416904084
>>> cm.V
0.5362013342441477
>>> cm.LambdaA
0.4
>>> cm.LambdaB
0.35714285714285715
>>> cm.Overall_ACC
0.6666666666666666
>>> cm = ConfusionMatrix(matrix={1:{1:495,0:405},0:{0:8645,1:455}}) # Verified Case - (Garcia et al., 2009)
>>> cm.ACC[1]
0.914
>>> cm.TNR[1]
0.95
>>> cm.TPR[1]
0.55
>>> cm.AUC[1]
0.75
>>> cm.AUPR[1]
0.5355263157894736
>>> cm.OP[1]
0.6473333333333334
>>> cm.IBA[1]
0.31350000000000006
>>> cm.IBA_alpha(0.5)[1]
0.41800000000000004
>>> cm.IBA_alpha(0.1)[1]
0.5016
>>> cm.GM[1]
0.722841614740048
>>> cm = ConfusionMatrix(matrix={1:{1:22,0:18},0:{1:2,0:14}}) # Verified Case - (https://bit.ly/2LiCZXB)
>>> cm.C
0.36170212765957444
>>> cm.Chi_Squared
8.429166666666667
>>> cm = ConfusionMatrix(matrix={0:{0:42,1:7},1:{1:114,0:203}}) # Verified Case - (https://bit.ly/2LiCZXB)
>>> cm.Q[0]
0.5422773393461104
>>> cm = ConfusionMatrix(matrix={0:{0:27,1:10},1:{0:16,1:15}})  # Verified Case - (https://bit.ly/2skyjKG)
>>> cm.Q[0]
0.4336283185840708
>>> cm.QI[0]
'Weak'
>>> cm = ConfusionMatrix(matrix={1:{1:828,0:72},0:{0:8918,1:182}}) # Verified Case - (Batuwita, Palade, 2009)
>>> cm.AGM[1]
0.9640451296531609
>>> cm.GM[1]
0.9495261976375375
>>> cm = ConfusionMatrix(matrix={1:{1:882,0:18},0:{0:8372,1:728}}) # Verified Case - (Batuwita, Palade, 2009)
>>> cm.AGM[1]
0.935458742218606
>>> cm.GM[1]
0.9495261976375375
>>> cm = ConfusionMatrix([1,2,3,2,3,3,1,2,2],[2,2,1,2,1,3,2,3,2])
>>> cm.F1_Macro
0.35555555555555557
>>> cm.F1_Micro
0.4444444444444444
>>> cm = ConfusionMatrix(matrix = {1:{1:5,0:1},0:{0:6,1:2}})
>>> cm.AGF[1]
0.8197822947299411
>>> cm.F2[1]
0.8064516129032258
>>> cm.F05[0]
0.8333333333333334
>>> cm = ConfusionMatrix(matrix={1:{1:53,0:2},0:{1:5,0:44}})
>>> cm.OC[1]
0.9636363636363636
>>> cm.OOC[1]
0.9383838571303771
>>> cm = ConfusionMatrix(matrix={1:{1:63,0:1},0:{0:50,1:2}})
>>> cm.TI(alpha=1,beta=1)[1]
0.9545454545454546
>>> cm.TI(alpha=0.5,beta=0.5)[1] == cm.F1[1]
True
>>> cm.TI(alpha=0.5,beta=0.5)[0] == cm.F1[0]
True
>>> cm.TI(alpha=2,beta=8)[1]
0.7777777777777778
>>> cm.TI(alpha=2,beta=8)[0]
0.8064516129032258
>>> cm = ConfusionMatrix(matrix={1:{1:22,0:54},0:{1:1,0:57}},transpose=True) # Verified Case -- (https://bit.ly/34KcVfB)
>>> cm.TPR[1]
0.9565217391304348
>>> cm.CI("TPR",0.05)[1][1][0]
0.8731774862637585
>>> cm.CI("TPR",0.05)[1][1][1]
1.0398659919971112
>>> cm.CI("TNR",0.05)[1][1][0]
0.4205300089203393
>>> cm.CI("TNR",0.05)[1][1][1]
0.6064970181066877
>>> cm.CI("PPV",0.05)[1][1][0]
0.18751037940411688
>>> cm.CI("PPV",0.05)[1][1][1]
0.3914369890169358
>>> cm.CI("NPV",0.05)[1][1][0]
0.9492581037307116
>>> cm.CI("NPV",0.05)[1][1][1]
1.0162591376485988
>>> cm.CI("Overall ACC",0.05)[1] == cm.CI95
True
>>> cm.CI("Kappa",0.05)[1]==cm.Kappa_CI
True
>>> cm.CI("TPR",0.01)[1][1][1]
1.0660599000409237
>>> cm.CI("TPR",0.01)[1][1][0]
0.8469835782199459
>>> cm.CI("TPR",0.02)[1][1][0]
0.8576142227182464
>>> cm.CI("TPR",0.02)[1][1][1]
1.0554292555426232
>>> cm.CI("TPR",0.1)[1][1][0]
0.8865720983316171
>>> cm.CI("TPR",0.1)[1][1][1]
1.0264713799292524
>>> cm.PLR[1]
1.966183574879227
>>> cm.NLR[1]
0.08466819221967958
>>> cm.CI("PLR")[1][1][1]
2.425775129875753
>>> cm.CI("PLR")[1][1][0]
1.5936670314213608
>>> cm.CI("NLR")[1][1][0]
0.012345468067066089
>>> cm.CI("NLR")[1][1][1]
0.5806748464136811
>>> cm.CI("PLR",0.01)[1][1][1]
2.591323998732794
>>> cm.CI("PLR",0.01)[1][1][0]
1.4918542999699553
>>> cm.CI("TPR",alpha=0.05,one_sided=True)[1][1][1]
1.0264713799292524
>>> cm.CI("TPR",alpha=0.1,one_sided=True)[1][1][1]
1.0109506389617338
>>> cm.CI("TPR",alpha=0.01,one_sided=True)[1][1][1]
1.0554292555426232
>>> cm.CI("TPR",alpha=0.005,one_sided=True)[1][1][1]
1.0660599000409237
>>> cm.CI("TPR",alpha=0.001,one_sided=True)[1][1][1]
1.0879165051294297
>>> cm.CI("TPR",alpha=0.0005,one_sided=True)[1][1][1]
1.0964210207280702
>>> cm.CI("ACC",alpha=0.05,one_sided=False)[1][1][1]
0.6728424118161956
>>> cm.CI("Overall ACC")[1][1] == cm.CI("ACC",alpha=0.05,one_sided=False)[1][1][1]
True
>>> cm.CI("FPR",0.05)[1][1][1]
0.5794699910796607
>>> cm.CI("FPR",0.05)[1][1][0]
0.39350298189331234
>>> cm.CI("FNR",0.05)[1][1][1]
0.12682251373624154
>>> cm.CI("FNR",0.05)[1][1][0]
-0.039865991997111175
>>> cm.CI("AUC")[1][1][0]
0.6361359326673304
>>> cm.CI("AUC")[1][1][1]
0.8338993199766178
>>> cm.CI("PRE")[1][1][0]
0.10779717474937288
>>> cm.CI("PRE")[1][1][1]
0.23548640734017934
>>> cm.CI("PRE",binom_method="wilson")[1][1][0]
0.11718265287943842
>>> cm.CI("PRE",binom_method="wilson")[1][1][1]
0.2444033995169354
>>> cm.CI("PRE",binom_method="agresti-coull")[1][1][0]
0.11654591925873323
>>> cm.CI("PRE",binom_method="agresti-coull")[1][1][1]
0.2450401331376406
>>> cm.CI("Overall ACC",binom_method="agresti-coull")[1][1]
0.6692525441184717
>>> cm.CI("Overall ACC",binom_method="agresti-coull")[1][0]
0.5048603506825172
>>> cm.CI("Overall ACC",binom_method="wilson")[1][1]
0.6692157009292735
>>> cm.CI("Overall ACC",binom_method="wilson")[1][0]
0.5048971938717156
>>> SE = AUC_SE_calc(0.88915,279,527) # Verified Case -- (https://bit.ly/2qblMrE)
>>> SE
0.011116012490627622
>>> CI_calc(0.88915,SE)[0]
0.8673626155183699
>>> CI_calc(0.88915,SE)[1]
0.9109373844816301
>>> cm = ConfusionMatrix(matrix={1:{1:135,0:48},0:{0:2014,1:1067}}) # Verified Case -- (Steyerberg et al., 2011, p. 792)
>>> cm.TP[1]
135
>>> cm.FP[1]
1067
>>> cm.POP[1]
3264
>>> cm.NB(w=0.059)[1]
0.022073223039215686
>>> cm = ConfusionMatrix(matrix={1:{1:3,2:0,3:1},2:{1:1,2:2,3:1},3:{1:0,2:2,3:2}})  # Verified Case -- (https://bit.ly/2ur7Rj4)
>>> cm.ARI
0.08333333333333333
>>> cm = ConfusionMatrix([0, 0, 1, 1], [0, 0, 1, 1]) # Verified Case -- (https://bit.ly/30PNzvL)
>>> cm.ARI
1.0
>>> cm = ConfusionMatrix([0, 0, 1, 2], [0, 0, 1, 1]) # Verified Case -- (https://bit.ly/30PNzvL)
>>> cm.ARI
0.5714285714285715
>>> cm = ConfusionMatrix([0, 1, 2, 0, 1, 2],[0, 2, 1, 0, 0, 1]) # Verified Case -- (https://bit.ly/3egZBEG)
>>> cm.weighted_average("F1")
0.26666666666666666
>>> cm = ConfusionMatrix([0, 1, 2, 2, 2],[0, 0, 2, 2, 1]) # Verified Case -- (https://bit.ly/2yidCBo)
>>> cm.average("PPV")
0.5
>>> cm.average("TPR")
0.5555555555555555
>>> cm.average("F1")
0.4888888888888889
>>> cm.weighted_average("PPV")
0.7
>>> cm.weighted_average("TPR")
0.6
>>> cm.weighted_average("F1")
0.6133333333333334
>>> cm = ConfusionMatrix(matrix={"often":{"often":16,"seldom":6,"never":2},"seldom":{"often":4,"seldom":10,"never":1},"never":{"often":3,"seldom":0,"never":8}}) # Verified Case -- (https://bit.ly/3btZm7z)
>>> cm.weighted_kappa(weight={"often":{"often":0,"seldom":1,"never":2},"seldom":{"often":1,"seldom":0,"never":1},"never":{"often":2,"seldom":1,"never":0}})
0.5009505703422054
>>> cm.weighted_kappa(weight={"often":{"often":0,"seldom":1,"never":1},"seldom":{"often":1,"seldom":0,"never":1},"never":{"often":1,"seldom":1,"never":0}})
0.49590422180214233
>>> cm = ConfusionMatrix(matrix={1:{1:60,2:10},2:{1:10,2:20}}) # Verified Case -- (Warrens, Raadt, 2019)
>>> cm.B
0.6896551724137931
>>> cm = ConfusionMatrix(matrix={1:{1:10,2:10,3:0},2:{1:10,2:10,3:0},3:{1:0,2:0,3:60}}) # Verified Case -- (Warrens, Raadt, 2019)
>>> cm.B
0.8636363636363636
>>> cm = ConfusionMatrix(matrix={1:{1:13,2:0,3:0},2:{1:0,2:20,3:7},3:{1:0,2:4,3:56}}) # Verified Case -- (https://bit.ly/3fWUuKF)
>>> cm.Alpha
0.7972584977308513
>>> cm.weighted_alpha(weight={1:{1:0,2:1,3:1},2:{1:1,2:0,3:1},3:{1:1,2:1,3:0}})
0.7972584977308516
>>> cm.Kappa
0.7964094021839719
>>> cm.PI
0.7962396962119107
>>> cm.AC1
0.8493305482313461
>>> cm = ConfusionMatrix(matrix={1:{1:55,2:10,3:2},2:{1:6,2:4,3:10},3:{1:2,2:5,3:6}}) # Verified Case -- (Gwet, Kilem L. Handbook of inter-rater reliability, 2014)
>>> cm.aickin_alpha()
0.40455288947232665
>>> cm = ConfusionMatrix(matrix={1:{1:60,0:40},0:{0:80,1:20}}) # Verified Case -- (https://bit.ly/3ooCi0t)
>>> cm.sensitivity_index()[1]
1.094968336708714
>>> y_true = np.array([0, 1, 1, 0])
>>> y_true_categorical = np.array(["spam", "ham", "ham", "spam"])
>>> y_prob = np.array([0.1, 0.9, 0.8, 0.3])
>>> cm1 = ConfusionMatrix(y_true, y_prob, threshold=lambda x: 1) # Verified Case -- (https://bit.ly/3n8Uo7R)
>>> cm1.brier_score()
0.03749999999999999
>>> cm1.brier_score(pos_class=1)
0.03749999999999999
>>> cm2 = ConfusionMatrix(y_true, 1-y_prob, threshold=lambda x: 1) # Verified Case -- (https://bit.ly/3n8Uo7R)
>>> cm2.brier_score(pos_class=0)
0.0375
>>> cm3 = ConfusionMatrix(y_true_categorical, y_prob, threshold=lambda x: "ham") # Verified Case -- (https://bit.ly/3n8Uo7R)
>>> cm3.brier_score(pos_class="ham")
0.03749999999999999
>>> cm4 = ConfusionMatrix(y_true, y_prob, sample_weight=[2,2,3,3],threshold=lambda x: 1)
>>> cm4.brier_score()
0.043
>>> cm5 = ConfusionMatrix(y_true, np.array(y_prob) > 0.5, threshold=lambda x: 1) # Verified Case -- (https://bit.ly/3n8Uo7R)
>>> cm5.brier_score()
0.0
"""
