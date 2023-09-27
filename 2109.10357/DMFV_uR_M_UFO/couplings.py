# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.0.0 for Linux x86 (64-bit) (April 7, 2019)
# Date: Tue 26 Sep 2023 12:51:36


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_7 = Coupling(name = 'GC_7',
                value = '-ee**2/(2.*cw)',
                order = {'QED':2})

GC_8 = Coupling(name = 'GC_8',
                value = '(ee**2*complex(0,1))/(2.*cw)',
                order = {'QED':2})

GC_9 = Coupling(name = 'GC_9',
                value = 'ee**2/(2.*cw)',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '-G',
                 order = {'QCD':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-(complex(0,1)*G)',
                 order = {'QCD':1})

GC_12 = Coupling(name = 'GC_12',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_13 = Coupling(name = 'GC_13',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '-2*complex(0,1)*lam',
                 order = {'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '-4*complex(0,1)*lam',
                 order = {'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = 'complex(0,1)*lambda1x1',
                 order = {'NP':1})

GC_18 = Coupling(name = 'GC_18',
                 value = 'complex(0,1)*lambda1x2',
                 order = {'NP':1})

GC_19 = Coupling(name = 'GC_19',
                 value = 'complex(0,1)*lambda1x3',
                 order = {'NP':1})

GC_20 = Coupling(name = 'GC_20',
                 value = 'complex(0,1)*lambda2x1',
                 order = {'NP':1})

GC_21 = Coupling(name = 'GC_21',
                 value = 'complex(0,1)*lambda2x2',
                 order = {'NP':1})

GC_22 = Coupling(name = 'GC_22',
                 value = 'complex(0,1)*lambda2x3',
                 order = {'NP':1})

GC_23 = Coupling(name = 'GC_23',
                 value = 'complex(0,1)*lambda3x1',
                 order = {'NP':1})

GC_24 = Coupling(name = 'GC_24',
                 value = 'complex(0,1)*lambda3x2',
                 order = {'NP':1})

GC_25 = Coupling(name = 'GC_25',
                 value = 'complex(0,1)*lambda3x3',
                 order = {'NP':1})

GC_26 = Coupling(name = 'GC_26',
                 value = 'complex(0,1)*lambdaHphi',
                 order = {'NP':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '4*complex(0,1)*lambdaphiphi',
                 order = {'NP':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '-ee/(2.*sw)',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '-(ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '(ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(CKM1x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '(CKM2x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '(CKM3x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '(CKM3x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '(CKM3x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-((cw*ee*complex(0,1))/sw)',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-ee**2/(2.*sw)',
                 order = {'QED':2})

GC_47 = Coupling(name = 'GC_47',
                 value = '-(ee**2*complex(0,1))/(2.*sw)',
                 order = {'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = 'ee**2/(2.*sw)',
                 order = {'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '(ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '-(cw*ee)/(2.*sw) - (ee*sw)/(2.*cw)',
                 order = {'QED':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '-(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '-(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw',
                 order = {'QED':2})

GC_59 = Coupling(name = 'GC_59',
                 value = '-(ee**2*complex(0,1)) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_61 = Coupling(name = 'GC_61',
                 value = '-(ee**2*vev)/(2.*cw)',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '(ee**2*vev)/(2.*cw)',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '-2*complex(0,1)*lam*vev',
                 order = {'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '-6*complex(0,1)*lam*vev',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = 'complex(0,1)*lambdaHphi*vev',
                 order = {'NP':1,'QED':-1})

GC_66 = Coupling(name = 'GC_66',
                 value = '-(ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '-(ee**2*complex(0,1)*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '(ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '-(ee**2*vev)/(2.*sw)',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '(ee**2*vev)/(2.*sw)',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '-(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '-(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '-(ee**2*complex(0,1)*vev)/2. - (cw**2*ee**2*complex(0,1)*vev)/(4.*sw**2) - (ee**2*complex(0,1)*sw**2*vev)/(4.*cw**2)',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = 'ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '-(yb/cmath.sqrt(2))',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '-(CKM1x3*yb)',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '-(CKM2x3*yb)',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '-(CKM3x3*yb)',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '-(yc/cmath.sqrt(2))',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '-((complex(0,1)*yc)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = 'yc/cmath.sqrt(2)',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = 'CKM2x1*yc',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = 'CKM2x2*yc',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = 'CKM2x3*yc',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '-(ydo/cmath.sqrt(2))',
                 order = {'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '-((complex(0,1)*ydo)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '-(CKM1x1*ydo)',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '-(CKM2x1*ydo)',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '-(CKM3x1*ydo)',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '-ye',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = 'ye',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '-(ye/cmath.sqrt(2))',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '-((complex(0,1)*ye)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '-ym',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = 'ym',
                 order = {'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '-(ym/cmath.sqrt(2))',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '-((complex(0,1)*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '-(ys/cmath.sqrt(2))',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '-((complex(0,1)*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '-(CKM1x2*ys)',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '-(CKM2x2*ys)',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '-(CKM3x2*ys)',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '-(yt/cmath.sqrt(2))',
                  order = {'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = 'yt/cmath.sqrt(2)',
                  order = {'QED':1})

GC_110 = Coupling(name = 'GC_110',
                  value = 'CKM3x1*yt',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = 'CKM3x2*yt',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = 'CKM3x3*yt',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '-ytau',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = 'ytau',
                  order = {'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '-(ytau/cmath.sqrt(2))',
                  order = {'QED':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '-(yup/cmath.sqrt(2))',
                  order = {'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '-((complex(0,1)*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = 'yup/cmath.sqrt(2)',
                  order = {'QED':1})

GC_120 = Coupling(name = 'GC_120',
                  value = 'CKM1x1*yup',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = 'CKM1x2*yup',
                  order = {'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = 'CKM1x3*yup',
                  order = {'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = 'ydo*complexconjugate(CKM1x1)',
                  order = {'QED':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '-(yup*complexconjugate(CKM1x1))',
                  order = {'QED':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = 'ys*complexconjugate(CKM1x2)',
                  order = {'QED':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '-(yup*complexconjugate(CKM1x2))',
                  order = {'QED':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_130 = Coupling(name = 'GC_130',
                  value = 'yb*complexconjugate(CKM1x3)',
                  order = {'QED':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '-(yup*complexconjugate(CKM1x3))',
                  order = {'QED':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '-(yc*complexconjugate(CKM2x1))',
                  order = {'QED':1})

GC_134 = Coupling(name = 'GC_134',
                  value = 'ydo*complexconjugate(CKM2x1)',
                  order = {'QED':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '-(yc*complexconjugate(CKM2x2))',
                  order = {'QED':1})

GC_137 = Coupling(name = 'GC_137',
                  value = 'ys*complexconjugate(CKM2x2)',
                  order = {'QED':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_139 = Coupling(name = 'GC_139',
                  value = 'yb*complexconjugate(CKM2x3)',
                  order = {'QED':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '-(yc*complexconjugate(CKM2x3))',
                  order = {'QED':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_142 = Coupling(name = 'GC_142',
                  value = 'ydo*complexconjugate(CKM3x1)',
                  order = {'QED':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '-(yt*complexconjugate(CKM3x1))',
                  order = {'QED':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_145 = Coupling(name = 'GC_145',
                  value = 'ys*complexconjugate(CKM3x2)',
                  order = {'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '-(yt*complexconjugate(CKM3x2))',
                  order = {'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = 'yb*complexconjugate(CKM3x3)',
                  order = {'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '-(yt*complexconjugate(CKM3x3))',
                  order = {'QED':1})

GC_150 = Coupling(name = 'GC_150',
                  value = 'complex(0,1)*complexconjugate(lambda1x1)',
                  order = {'NP':1})

GC_151 = Coupling(name = 'GC_151',
                  value = 'complex(0,1)*complexconjugate(lambda1x2)',
                  order = {'NP':1})

GC_152 = Coupling(name = 'GC_152',
                  value = 'complex(0,1)*complexconjugate(lambda1x3)',
                  order = {'NP':1})

GC_153 = Coupling(name = 'GC_153',
                  value = 'complex(0,1)*complexconjugate(lambda2x1)',
                  order = {'NP':1})

GC_154 = Coupling(name = 'GC_154',
                  value = 'complex(0,1)*complexconjugate(lambda2x2)',
                  order = {'NP':1})

GC_155 = Coupling(name = 'GC_155',
                  value = 'complex(0,1)*complexconjugate(lambda2x3)',
                  order = {'NP':1})

GC_156 = Coupling(name = 'GC_156',
                  value = 'complex(0,1)*complexconjugate(lambda3x1)',
                  order = {'NP':1})

GC_157 = Coupling(name = 'GC_157',
                  value = 'complex(0,1)*complexconjugate(lambda3x2)',
                  order = {'NP':1})

GC_158 = Coupling(name = 'GC_158',
                  value = 'complex(0,1)*complexconjugate(lambda3x3)',
                  order = {'NP':1})

