- **silence_to_tonic.dat**: Isopotential model (XPP). Start at I=-1.95 pA, increase in 0.01 pA steps, let system settle for 5 s each time. In XPP:

		global 1 t-10 {I=-1.95}
		global 1 t-5000 {I=-1.94}
		global 1 t-10000 {I=-1.93}
		global 1 t-15000 {I=-1.92}
		global 1 t-20000 {I=-1.91}
		global 1 t-25000 {I=-1.90}


- **tonic_to_silence.dat**: Isopotential model (XPP). Start at I=-1.80 pA to generate spiking, then go to I=-2.70 pA* and decrease in 0.01 pA steps, let system settle for 5 s each time. In XPP:

		global 1 t-10 {I=-1.80}
		global 1 t-5000 {I=-2.70}
		global 1 t-10000 {I=-2.71}
		global 1 t-15000 {I=-2.72}
		global 1 t-20000 {I=-2.73}
		global 1 t-25000 {I=-2.74}

  \* Finer increments between -1.80 pA and -2.70 pA did not affect the results