import numpy as np
import scipy.stats
import math

import matplotlib.pyplot as plt
from scipy.interpolate import griddata

from sklearn.preprocessing import MinMaxScaler
from sklearn.manifold import TSNE
import tensorflow as tf

class NeuralResponseMap():
    def __init__(self, model):
        self.model = model

        self.activation_model = None
        self.normalization = None
        self.neurons = None
        self.projection = None

    def GenerateActivations(self, inputs):
        full_output = []
        activations = self.activation_model.predict(inputs) 
        activations = [activations] if type(activations)!=type([]) else activations
        for inp in range(len(inputs)):
            output = np.array([])
            for i in range(len(activations)):
                activation = activations[i][inp]
                if len(activation.shape)==3:
                    activation = activation.mean(axis=(0,1))
                output = np.concatenate([output, activation])
            full_output.append(output)
        full_output = np.array(full_output)  
        return full_output       
        
    def TrainMap(self, inputs, layers=None):
        layers = self.model.layers[1:-1] if layers==None else layers
        outputs = [layer.output for layer in layers] 
        self.activation_model = tf.keras.models.Model(inputs=self.model.input, outputs=outputs) 

        full_output = self.GenerateActivations(inputs) 
        self.normalization = MinMaxScaler((0,1)).fit(full_output)
        full_output = self.normalization.transform(full_output)

        self.neurons = np.array([len(set(x))>1 for x in full_output.T])
        full_output = full_output[:,self.neurons]

        correlation, _ = scipy.stats.spearmanr(full_output)
        self.projection = TSNE(metric='precomputed', square_distances=True).fit_transform(1-correlation)
        self.projection = MinMaxScaler((-1,1)).fit_transform(self.projection)
        
    def GenerateMap(self, inputs, method='nearest', cmap='viridis', size=(5,5), file=None):
        full_output = self.GenerateActivations(inputs)
        full_output = self.normalization.transform(full_output)
        full_output = full_output[:,self.neurons]
        Z = np.clip(full_output,0,1).mean(axis=0)

        x = np.linspace(self.projection[:,0].min(), self.projection[:,0].max(), 1000)
        y = np.linspace(self.projection[:,1].min(), self.projection[:,1].max(), 1000)
        grid_x, grid_y = np.meshgrid(x,y)

        if method=='nearest':
            filtering = griddata(self.projection, Z, (grid_x,grid_y), method='linear')
            grid_z = griddata(self.projection, Z, (grid_x,grid_y), method='nearest')
            grid_z[np.isnan(filtering)]=float('nan')
        else:
            grid_z = griddata(self.projection, Z, (grid_x,grid_y), method='linear')

        fig = plt.figure(figsize=size)
        plt.imshow(grid_z, vmin=0, vmax=1, cmap=cmap)
        plt.axis('off');

        if file!=None:
            fig.savefig(file)

    def CircleProjection(self):
        angles = np.array([math.atan2(proj[1],proj[0]) for proj in self.projection])
        angles = np.round((angles+np.pi)/(2*np.pi),2)
        
        for i in range(len(self.projection)):
            norm = np.abs(self.projection[angles==angles[i]]).max(axis=0)
            self.projection[i] = self.projection[i]/np.sqrt(sum(norm**2))
