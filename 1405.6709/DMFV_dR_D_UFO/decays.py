# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.0.0 for Linux x86 (64-bit) (April 7, 2019)
# Date: Tue 26 Sep 2023 11:00:20


from object_library import all_decays, Decay
import particles as P


Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.phi,P.chi1):'((3*lambda3x1*MB**2*complexconjugate(lambda3x1) + 3*lambda3x1*mchi1**2*complexconjugate(lambda3x1) - 3*lambda3x1*Mphi**2*complexconjugate(lambda3x1))*cmath.sqrt(MB**4 - 2*MB**2*mchi1**2 + mchi1**4 - 2*MB**2*Mphi**2 - 2*mchi1**2*Mphi**2 + Mphi**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.phi,P.chi2):'((3*lambda3x2*MB**2*complexconjugate(lambda3x2) + 3*lambda3x2*mchi2**2*complexconjugate(lambda3x2) - 3*lambda3x2*Mphi**2*complexconjugate(lambda3x2))*cmath.sqrt(MB**4 - 2*MB**2*mchi2**2 + mchi2**4 - 2*MB**2*Mphi**2 - 2*mchi2**2*Mphi**2 + Mphi**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.phi,P.chi3):'((3*lambda3x3*MB**2*complexconjugate(lambda3x3) + 3*lambda3x3*mchi3**2*complexconjugate(lambda3x3) - 3*lambda3x3*Mphi**2*complexconjugate(lambda3x3))*cmath.sqrt(MB**4 - 2*MB**2*mchi3**2 + mchi3**4 - 2*MB**2*Mphi**2 - 2*mchi3**2*Mphi**2 + Mphi**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.W__minus__,P.t):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_chi1 = Decay(name = 'Decay_chi1',
                   particle = P.chi1,
                   partial_widths = {(P.phi__tilde__,P.b):'((3*lambda3x1*MB**2*complexconjugate(lambda3x1) + 3*lambda3x1*mchi1**2*complexconjugate(lambda3x1) - 3*lambda3x1*Mphi**2*complexconjugate(lambda3x1))*cmath.sqrt(MB**4 - 2*MB**2*mchi1**2 + mchi1**4 - 2*MB**2*Mphi**2 - 2*mchi1**2*Mphi**2 + Mphi**4))/(32.*cmath.pi*abs(mchi1)**3)',
                                     (P.phi__tilde__,P.d):'((mchi1**2 - Mphi**2)*(3*lambda1x1*mchi1**2*complexconjugate(lambda1x1) - 3*lambda1x1*Mphi**2*complexconjugate(lambda1x1)))/(32.*cmath.pi*abs(mchi1)**3)',
                                     (P.phi__tilde__,P.s):'((mchi1**2 - Mphi**2)*(3*lambda2x1*mchi1**2*complexconjugate(lambda2x1) - 3*lambda2x1*Mphi**2*complexconjugate(lambda2x1)))/(32.*cmath.pi*abs(mchi1)**3)'})

Decay_chi2 = Decay(name = 'Decay_chi2',
                   particle = P.chi2,
                   partial_widths = {(P.phi__tilde__,P.b):'((3*lambda3x2*MB**2*complexconjugate(lambda3x2) + 3*lambda3x2*mchi2**2*complexconjugate(lambda3x2) - 3*lambda3x2*Mphi**2*complexconjugate(lambda3x2))*cmath.sqrt(MB**4 - 2*MB**2*mchi2**2 + mchi2**4 - 2*MB**2*Mphi**2 - 2*mchi2**2*Mphi**2 + Mphi**4))/(32.*cmath.pi*abs(mchi2)**3)',
                                     (P.phi__tilde__,P.d):'((mchi2**2 - Mphi**2)*(3*lambda1x2*mchi2**2*complexconjugate(lambda1x2) - 3*lambda1x2*Mphi**2*complexconjugate(lambda1x2)))/(32.*cmath.pi*abs(mchi2)**3)',
                                     (P.phi__tilde__,P.s):'((mchi2**2 - Mphi**2)*(3*lambda2x2*mchi2**2*complexconjugate(lambda2x2) - 3*lambda2x2*Mphi**2*complexconjugate(lambda2x2)))/(32.*cmath.pi*abs(mchi2)**3)'})

Decay_chi3 = Decay(name = 'Decay_chi3',
                   particle = P.chi3,
                   partial_widths = {(P.phi__tilde__,P.b):'((3*lambda3x3*MB**2*complexconjugate(lambda3x3) + 3*lambda3x3*mchi3**2*complexconjugate(lambda3x3) - 3*lambda3x3*Mphi**2*complexconjugate(lambda3x3))*cmath.sqrt(MB**4 - 2*MB**2*mchi3**2 + mchi3**4 - 2*MB**2*Mphi**2 - 2*mchi3**2*Mphi**2 + Mphi**4))/(32.*cmath.pi*abs(mchi3)**3)',
                                     (P.phi__tilde__,P.d):'((mchi3**2 - Mphi**2)*(3*lambda1x3*mchi3**2*complexconjugate(lambda1x3) - 3*lambda1x3*Mphi**2*complexconjugate(lambda1x3)))/(32.*cmath.pi*abs(mchi3)**3)',
                                     (P.phi__tilde__,P.s):'((mchi3**2 - Mphi**2)*(3*lambda2x3*mchi3**2*complexconjugate(lambda2x3) - 3*lambda2x3*Mphi**2*complexconjugate(lambda2x3)))/(32.*cmath.pi*abs(mchi3)**3)'})

Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.b,P.b__tilde__):'((-12*MB**2*yb**2 + 3*MH**2*yb**2)*cmath.sqrt(-4*MB**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.phi__tilde__,P.phi):'(lambdaHphi**2*vev**2*cmath.sqrt(MH**4 - 4*MH**2*Mphi**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_phi = Decay(name = 'Decay_phi',
                  particle = P.phi,
                  partial_widths = {(P.b,P.chi1__tilde__):'((-3*lambda3x1*MB**2*complexconjugate(lambda3x1) - 3*lambda3x1*mchi1**2*complexconjugate(lambda3x1) + 3*lambda3x1*Mphi**2*complexconjugate(lambda3x1))*cmath.sqrt(MB**4 - 2*MB**2*mchi1**2 + mchi1**4 - 2*MB**2*Mphi**2 - 2*mchi1**2*Mphi**2 + Mphi**4))/(48.*cmath.pi*abs(Mphi)**3)',
                                    (P.b,P.chi2__tilde__):'((-3*lambda3x2*MB**2*complexconjugate(lambda3x2) - 3*lambda3x2*mchi2**2*complexconjugate(lambda3x2) + 3*lambda3x2*Mphi**2*complexconjugate(lambda3x2))*cmath.sqrt(MB**4 - 2*MB**2*mchi2**2 + mchi2**4 - 2*MB**2*Mphi**2 - 2*mchi2**2*Mphi**2 + Mphi**4))/(48.*cmath.pi*abs(Mphi)**3)',
                                    (P.b,P.chi3__tilde__):'((-3*lambda3x3*MB**2*complexconjugate(lambda3x3) - 3*lambda3x3*mchi3**2*complexconjugate(lambda3x3) + 3*lambda3x3*Mphi**2*complexconjugate(lambda3x3))*cmath.sqrt(MB**4 - 2*MB**2*mchi3**2 + mchi3**4 - 2*MB**2*Mphi**2 - 2*mchi3**2*Mphi**2 + Mphi**4))/(48.*cmath.pi*abs(Mphi)**3)',
                                    (P.d,P.chi1__tilde__):'((-mchi1**2 + Mphi**2)*(-3*lambda1x1*mchi1**2*complexconjugate(lambda1x1) + 3*lambda1x1*Mphi**2*complexconjugate(lambda1x1)))/(48.*cmath.pi*abs(Mphi)**3)',
                                    (P.d,P.chi2__tilde__):'((-mchi2**2 + Mphi**2)*(-3*lambda1x2*mchi2**2*complexconjugate(lambda1x2) + 3*lambda1x2*Mphi**2*complexconjugate(lambda1x2)))/(48.*cmath.pi*abs(Mphi)**3)',
                                    (P.d,P.chi3__tilde__):'((-mchi3**2 + Mphi**2)*(-3*lambda1x3*mchi3**2*complexconjugate(lambda1x3) + 3*lambda1x3*Mphi**2*complexconjugate(lambda1x3)))/(48.*cmath.pi*abs(Mphi)**3)',
                                    (P.s,P.chi1__tilde__):'((-mchi1**2 + Mphi**2)*(-3*lambda2x1*mchi1**2*complexconjugate(lambda2x1) + 3*lambda2x1*Mphi**2*complexconjugate(lambda2x1)))/(48.*cmath.pi*abs(Mphi)**3)',
                                    (P.s,P.chi2__tilde__):'((-mchi2**2 + Mphi**2)*(-3*lambda2x2*mchi2**2*complexconjugate(lambda2x2) + 3*lambda2x2*Mphi**2*complexconjugate(lambda2x2)))/(48.*cmath.pi*abs(Mphi)**3)',
                                    (P.s,P.chi3__tilde__):'((-mchi3**2 + Mphi**2)*(-3*lambda2x3*mchi3**2*complexconjugate(lambda2x3) + 3*lambda2x3*Mphi**2*complexconjugate(lambda2x3)))/(48.*cmath.pi*abs(Mphi)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.s__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*ee**2*MB**2)/(2.*sw**2) - (3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MB**4)/(2.*MW**2*sw**2) + (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-(ee**2*MTA**2)/(2.*sw**2) - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

