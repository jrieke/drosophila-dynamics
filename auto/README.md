- **bifurcation_diagram.ipynb**: Jupyter notebook to run numerical continuation in one parameter (*I*)

- **2par_gxxx.ipynb**: Jupyter notebook to run numerical continuation in two parameters (*I* and *gxxx*)

- **continuation_functions.py**: Convenience functions to run numerical continuation in AUTO and plot the results. The Jupyter notebooks above import this file and use the functions. 

- **plot_eigenvalues.ipynb**: Jupyter notebook to read eigenvalues from AUTO's fort.9 file and plot them in the complex plane.

- **auto_files**: Contains all files for AUTO, namely the model definition (**drosophila.c**) and the constant files (**c.xxx**). Usually, it should not be necessary to use these files directly, as they are wrapped by the convenience functions in **continuation_functions.py**.

- **plots**: Contains the bifurcation diagrams. 