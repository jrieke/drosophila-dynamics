- **increasing.dat**: Isopotential model (XPP). Multiple current steps with increasing amplitudes, in XPP: 

   		global 1 t-10 {I=-1.9}
      global 1 t-3500 {I=-1}
      global 1 t-4000 {I=0}
      global 1 t-4500 {I=5}
      global 1 t-5000 {I=10}
      global 1 t-5500 {I=15}
      global 1 t-6000 {I=20}
      global 1 t-6500 {I=25}
      global 1 t-7000 {I=30}
      global 1 t-7500 {I=35}
      global 1 t-8000 {I=40}
      global 1 t-8500 {I=45}
      global 1 t-9000 {I=50}
      global 1 t-9500 {I=55}
      global 1 t-10000 {I=59}

  Columns: t / ms, V / mV, gating variables and currents


- **decreasing.dat**: Isopotential model (XPP). Multiple current steps with decreasing amplitudes, in XPP: 

  		global 1 t-10 {I=0}   
      global 1 t-500 {I=-2.2}  
      global 1 t-1000 {I=-2.5} 
      global 1 t-1500 {I=-2.72}

  Columns: t / ms, V / mV, gating variables and currents
