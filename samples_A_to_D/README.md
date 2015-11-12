Set ```nout=10``` for all runs to have more points for the trajectories in phase space. 

```total=230```; ```Ihold=-12```; ```Ipulse``` equals value in file name

- **3pA.dat** and **65pA.dat**: In XPP:
		
		global 1 t-10 {I=Ipulse}
		global 1 t-210 {I=Ihold}

- **-5pA_with_square_pulse.dat**: In XPP:

		global 1 t-10 {I=Ipulse}
		global 1 t-75 {I=Ipulse+25}
		global 1 t-80 {I=Ipulse}
		global 1 t-210 {I=Ihold}

- **-2.2pA_with_square_pulses.dat**: In XPP:

		global 1 t-10 {I=Ipulse}
		global 1 t-65 {I=Ipulse+15}
		global 1 t-70 {I=Ipulse}
		global 1 t-160 {I=Ipulse-15}
		global 1 t-165 {I=Ipulse}
		global 1 t-210 {I=Ihold}
