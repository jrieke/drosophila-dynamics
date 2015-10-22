#include "auto_f2c.h"
#include "drosophila.h"
#include <math.h>
/* --------------------------------------------------------------------- */
/*  drosophila motoneurone                                               */
/*  https://senselab.med.yale.edu/ModelDB/ShowModel.cshtml?model=152028  */
/* --------------------------------------------------------------------- */
int func (integer ndim, const doublereal *u, const integer *icp,
          const doublereal *par, integer ijac,
          doublereal *f, doublereal *dfdu, doublereal *dfdp)
{


    double I = par[0];
    // double gKs = par[1];
    // double EK = par[2];
    // double gKf = par[3];
    // double fh = par[4];
    // double ENa = par[5];
    // double gNa = par[6];
    // double gNaP = par[7];
    double gleak = par[1];
    double Eleak = par[2];

    double V = u[0];
    double mKs = u[1];
    double mKf = u[2];
    double hKf = u[3];
    double hKf2 = u[4];
    double mNa = u[5];
    double hNa = u[6];
    double mNaP = u[7];

    double minfKs = 1./(1.+exp((V+12.85)/(-19.91)));
    double mtauKs = 2.03 + 1.96 /(1.+exp((V-29.83)/3.32));

    double minfKf = 1./(1.+exp((V+17.55)/(-7.27)));
    double mtauKf = 1.94+2.66/(1.+exp((V-8.12)/7.96));

    double hinfK = 1./(1.+exp((V+45.)/6.));
    double htauK = 1.79+515.8/(1.+exp((V+147.4)/(28.66)));
    //comment in original code: # mistake; should be hinfK == hinfK2
    double hinfK2 = 1./(1.+exp((V+44.2)/1.5));

    double minfNa = 1./(1.+exp((V+29.13)/(-8.922)));
    double mtauNa = 3.861-3.434/(1.+exp((V+51.35)/(-5.98)));
    double hinfNa = 1./(1.+exp((V+40.)/6.048));
    double htauNa = 2.834-2.371/(1.+exp((V+21.9)/(-2.641)));

    double minfNaP = 1./(1.+exp((V+48.77)/(-3.68)));
    double mtauNaP = 1.;

    double Iks = gKs*pow(mKs,4)*(V-EK);
    double Ikf = gKf*pow(mKf,4)*(fh*hKf + (1.-fh)*hKf2)*(V-EK);
    double Ina = gNa*pow(mNa,3)*hNa*(V-ENa);
    double Inap= gNaP*mNaP*(V-ENa);


    f[0] = -1./c*(Iks+Ikf+Ina+Inap+gleak*(V-Eleak)-I);
    f[1] = (minfKs-mKs)/mtauKs;
    f[2] = (minfKf-mKf)/mtauKf;
    f[3] = (hinfK-hKf)/htauK;
    f[4] = (hinfK2-hKf2)/116.;
    f[5] = (minfNa-mNa)/mtauNa;
    f[6] = (hinfNa-hNa)/htauNa;
    f[7] = (minfNaP-mNaP)/mtauNaP;

  return 0;
}
/* ---------------------------------------------------------------------- */
/* ---------------------------------------------------------------------- */
int stpnt (integer ndim, doublereal t,
           doublereal *u, doublereal *par)
{


  par[0] = I_0;
  par[1] = gleak_0;
  par[2] = Eleak_0;

  /* steady state for I_0 = -12, from xpp code  */
  u[0] = -54.56137733296305;
  u[1] = 0.1095841015345856;
  u[2] = 0.006114411948700807;
  u[3] = 0.831116786237579;
  u[4] = 0.331878827270821;
  u[5] = 0.05466001581199555;
  u[6] = 0.9174076713170543;
  u[7] = 0.1716833324516358;


  return 0;
}
/* ---------------------------------------------------------------------- */
/* ---------------------------------------------------------------------- */
int pvls (integer ndim, const doublereal *u, doublereal *par)
{

  double V = u[0];
  double mKs = u[1];
  double mKf = u[2];
  double hKf = u[3];
  double hKf2 = u[4];
  double mNa = u[5];
  double hNa = u[6];
  double mNaP = u[7];

  double Iks = gKs*pow(mKs,4)*(V-EK);
  double Ikf = gKf*pow(mKf,4)*(fh*hKf + (1.-fh)*hKf2)*(V-EK);
  double Ina = gNa*pow(mNa,3)*hNa*(V-ENa);
  double Inap= gNaP*mNaP*(V-ENa);

  doublereal f = 1.0/par[10];
  par[NP] = isnan(f) ? 0.0 : f;

  par[NP+1] = Iks;
  par[NP+2] = Ikf;
  par[NP+3] = Ina;
  par[NP+4] = Inap;

  return 0;
}
/* ---------------------------------------------------------------------- */
/* ---------------------------------------------------------------------- */
int bcnd (integer ndim, const doublereal *par, const integer *icp,
          integer nbc, const doublereal *u0, const doublereal *u1, integer ijac,
          doublereal *fb, doublereal *dbc)
{
  return 0;
}
/* ---------------------------------------------------------------------- */
/* ---------------------------------------------------------------------- */
int icnd (integer ndim, const doublereal *par, const integer *icp,
          integer nint, const doublereal *u, const doublereal *uold,
          const doublereal *udot, const doublereal *upold, integer ijac,
          doublereal *fi, doublereal *dint)
{
  return 0;
}
/* ---------------------------------------------------------------------- */
/* ---------------------------------------------------------------------- */
int fopt (integer ndim, const doublereal *u, const integer *icp,
          const doublereal *par, integer ijac,
          doublereal *fs, doublereal *dfdu, doublereal *dfdp)
{
  return 0;
}
/* ---------------------------------------------------------------------- */
/* ---------------------------------------------------------------------- */
