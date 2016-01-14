Isopotential model (XPP). Start with constant current step (with amplitude Ihold, see below), then apply short square current pulse (10 ms, 48 pA for exciting pulse or -72 pA for inhibiting pulse).


- **-2.72pA.dat and -2.73pA.dat**: Filename equals Ihold. In XPP:

		global 1 t-10 {I=Ihold}
		global 1 t-250 {I=48}
		global 1 t-260 {I=Ihold}

- **-1.90pA.dat and -1.91pA.dat**: Filename equals Ihold. Make model fire first by applying I=0 before the constant current step. In XPP:

		global 1 t-10 {I=0}
		global 1 t-100 {I=Ihold}
		global 1 t-350 {I=-72}
		global 1 t-360 {I=Ihold}
