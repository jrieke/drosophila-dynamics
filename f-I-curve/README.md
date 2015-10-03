- **/separate runs**: Isopotential model (NeuroML2). Current pulse from 10 ms to 510 ms with varying amplitudes (see file names). Spike times extracted from OMV tests at a threshold of -25 mV (see *spike times.txt*). Columns in .dat files: t / s, V / V, I / A


- **increasing.dat**: Isopotential model (XPP). Multiple current steps with increasing amplitudes, in XPP: 

   		global 1 t-10 {I=-1.9}
   		global 1 t-3500 {I=-1.7}
   		global 1 t-4000 {I=-1.2}
   		global 1 t-4500 {I=-0.5}
   		global 1 t-5000 {I=0}
   		global 1 t-5500 {I=5}
   		global 1 t-6000 {I=10}
   		global 1 t-6500 {I=15}
   		global 1 t-7000 {I=20}
   		global 1 t-7500 {I=25}
   		global 1 t-8000 {I=30}
   		global 1 t-8500 {I=35}
   		global 1 t-9000 {I=40}
   		global 1 t-9500 {I=45}
   		global 1 t-10000 {I=50}

  Columns: t / ms, V / mV, gating variables and currents


- **decreasing.dat**: Isopotential model (XPP). Multiple current steps with decreasing amplitudes, in XPP: 

		global 1 t-10 {I=50}   
		global 1 t-500 {I=45}  
		global 1 t-1000 {I=40}  
		global 1 t-1500 {I=35}  
		global 1 t-2000 {I=30}  
		global 1 t-2500 {I=25}  
		global 1 t-3000 {I=20}  
		global 1 t-3500 {I=15}  
		global 1 t-4000 {I=10}  
		global 1 t-4500 {I=5}  
		global 1 t-5000 {I=0}  
		global 1 t-5500 {I=-1.2}  
		global 1 t-6000 {I=-1.9}  
		global 1 t-6500 {I=-2.4}
		global 1 t-7000 {I=-2.7}  
		global 1 t-7500 {I=-2.72}

  Columns: t / ms, V / mV, gating variables and currents
