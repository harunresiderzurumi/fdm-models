# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.0.0 for Linux x86 (64-bit) (April 7, 2019)
# Date: Tue 26 Sep 2023 12:02:07



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

Rel11 = Parameter(name = 'Rel11',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Rel11}',
                  lhablock = 'FRBlock',
                  lhacode = [ 1 ])

Rel12 = Parameter(name = 'Rel12',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Rel12}',
                  lhablock = 'FRBlock',
                  lhacode = [ 2 ])

Rel13 = Parameter(name = 'Rel13',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Rel13}',
                  lhablock = 'FRBlock',
                  lhacode = [ 3 ])

Rel21 = Parameter(name = 'Rel21',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Rel21}',
                  lhablock = 'FRBlock',
                  lhacode = [ 4 ])

Rel22 = Parameter(name = 'Rel22',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Rel22}',
                  lhablock = 'FRBlock',
                  lhacode = [ 5 ])

Rel23 = Parameter(name = 'Rel23',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Rel23}',
                  lhablock = 'FRBlock',
                  lhacode = [ 6 ])

Rel31 = Parameter(name = 'Rel31',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Rel31}',
                  lhablock = 'FRBlock',
                  lhacode = [ 7 ])

Rel32 = Parameter(name = 'Rel32',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Rel32}',
                  lhablock = 'FRBlock',
                  lhacode = [ 8 ])

Rel33 = Parameter(name = 'Rel33',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Rel33}',
                  lhablock = 'FRBlock',
                  lhacode = [ 9 ])

Iml11 = Parameter(name = 'Iml11',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Iml11}',
                  lhablock = 'FRBlock',
                  lhacode = [ 10 ])

Iml12 = Parameter(name = 'Iml12',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Iml12}',
                  lhablock = 'FRBlock',
                  lhacode = [ 11 ])

Iml13 = Parameter(name = 'Iml13',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Iml13}',
                  lhablock = 'FRBlock',
                  lhacode = [ 12 ])

Iml21 = Parameter(name = 'Iml21',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Iml21}',
                  lhablock = 'FRBlock',
                  lhacode = [ 13 ])

Iml22 = Parameter(name = 'Iml22',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Iml22}',
                  lhablock = 'FRBlock',
                  lhacode = [ 14 ])

Iml23 = Parameter(name = 'Iml23',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Iml23}',
                  lhablock = 'FRBlock',
                  lhacode = [ 15 ])

Iml31 = Parameter(name = 'Iml31',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Iml31}',
                  lhablock = 'FRBlock',
                  lhacode = [ 16 ])

Iml32 = Parameter(name = 'Iml32',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Iml32}',
                  lhablock = 'FRBlock',
                  lhacode = [ 17 ])

Iml33 = Parameter(name = 'Iml33',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{Iml33}',
                  lhablock = 'FRBlock',
                  lhacode = [ 18 ])

lH1 = Parameter(name = 'lH1',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{lH1}',
                lhablock = 'FRBlock',
                lhacode = [ 19 ])

lH2 = Parameter(name = 'lH2',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{lH2}',
                lhablock = 'FRBlock',
                lhacode = [ 20 ])

lH3 = Parameter(name = 'lH3',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{lH3}',
                lhablock = 'FRBlock',
                lhacode = [ 21 ])

lambdaphiphi = Parameter(name = 'lambdaphiphi',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{lambdaphiphi}',
                         lhablock = 'FRBlock',
                         lhacode = [ 22 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

Mpsi = Parameter(name = 'Mpsi',
                 nature = 'external',
                 type = 'real',
                 value = 500,
                 texname = '\\text{Mpsi}',
                 lhablock = 'MASS',
                 lhacode = [ 9000005 ])

mphi1 = Parameter(name = 'mphi1',
                  nature = 'external',
                  type = 'real',
                  value = 200,
                  texname = '\\text{mphi1}',
                  lhablock = 'MASS',
                  lhacode = [ 9000006 ])

mphi2 = Parameter(name = 'mphi2',
                  nature = 'external',
                  type = 'real',
                  value = 200,
                  texname = '\\text{mphi2}',
                  lhablock = 'MASS',
                  lhacode = [ 9000007 ])

mphi3 = Parameter(name = 'mphi3',
                  nature = 'external',
                  type = 'real',
                  value = 200,
                  texname = '\\text{mphi3}',
                  lhablock = 'MASS',
                  lhacode = [ 9000008 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

Wpsi = Parameter(name = 'Wpsi',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{Wpsi}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000005 ])

wphi1 = Parameter(name = 'wphi1',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{wphi1}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000006 ])

wphi2 = Parameter(name = 'wphi2',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{wphi2}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000007 ])

wphi3 = Parameter(name = 'wphi3',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{wphi3}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000008 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

lambda1x1 = Parameter(name = 'lambda1x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*Iml11 + Rel11',
                      texname = '\\text{lambda1x1}')

lambda1x2 = Parameter(name = 'lambda1x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*Iml12 + Rel12',
                      texname = '\\text{lambda1x2}')

lambda1x3 = Parameter(name = 'lambda1x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*Iml13 + Rel13',
                      texname = '\\text{lambda1x3}')

lambda2x1 = Parameter(name = 'lambda2x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*Iml21 + Rel21',
                      texname = '\\text{lambda2x1}')

lambda2x2 = Parameter(name = 'lambda2x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*Iml22 + Rel22',
                      texname = '\\text{lambda2x2}')

lambda2x3 = Parameter(name = 'lambda2x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*Iml23 + Rel23',
                      texname = '\\text{lambda2x3}')

lambda3x1 = Parameter(name = 'lambda3x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*Iml31 + Rel31',
                      texname = '\\text{lambda3x1}')

lambda3x2 = Parameter(name = 'lambda3x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*Iml32 + Rel32',
                      texname = '\\text{lambda3x2}')

lambda3x3 = Parameter(name = 'lambda3x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*Iml33 + Rel33',
                      texname = '\\text{lambda3x3}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

