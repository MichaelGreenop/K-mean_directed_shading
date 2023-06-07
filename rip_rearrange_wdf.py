
"""This is a module used for the selection of different sections of the Raman
image, and also removing the background from the Raman image.

Both 2 and 3D slices"""

# You need to take the code from Kmean_Background in the Z. Python_modules
# file of the passport 


from renishawWiRE import WDFReader
import common_functions_wdf as cf
import pandas as pd
import numpy as np


class rearrange2D:
    """"""
    
    def __init__(self, name):
        
        self.name = name
               
        
    def img(self):
        reader = WDFReader(self.name)
        spectra = reader.spectra
        shp = spectra.shape
        return int(shp[0]), int(shp[1])
           

        
class rearrange3D_slice:
    """"""
    
    def __init__(self, name):
        
        self.name = name
        
        
    def slice3D(self):
        df = cf.one_variable(self.name).raw()
        y = df['Unnamed: 1']
        Y = int(len(y.unique()))
        x = df['#X']
        X = int(len(x.unique()))
        full = cf.one_variable(self.name).FullNum()
        XY = cf.one_variable(self.name).NumSpec()
        w = len(cf.one_variable(self.name).waves())
        Z = full/XY/w
        return (int(Z),int(Y),int(X)) 
   
    
class rearrange3D_stack:
    """"""
    
    def __init__(self, name):
        
        self.name = name
        
        
    def stack3D(self):
        df = cf.one_variable(self.name).raw()
        y = df['Unnamed: 1']
        Y = int(len(y.unique()))
        x = df['#X']
        X = int(len(x.unique()))
        full = cf.one_variable(self.name).FullNum()
        XY = cf.one_variable(self.name).NumSpec()
        w = len(cf.one_variable(self.name).waves())
        Z = full/XY/w
        return (int(Z*Y),int(X)) 
    
    
    
 