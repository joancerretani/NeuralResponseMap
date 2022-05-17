# Neural Response Map

## Project Description
---

Neural Response Map is a tool that allows you to graphically detect the activations of artificial neural networks. To do this, the correlation between neuron activations is calculated and then t-SNE is applied to reduce the dimension. In this way the correlated neurons are plotted close to each other. This process allows observing the activation of neurons and obtaining the response to different stimuli such as the graphs presented by DeepMind in his [paper](https://arxiv.org/pdf/1807.01281.pdf).

<p align="center">
    <img src="https://github.com/joancerretani/NeuralResponseMap/blob/main/examples/neuralmap1.png">
</p>

## Instalation
---

To install you can use the following command

```python
pip install neural-response-map
```

## Quick Start
---

To make use of the tool, first import the components

```python
from neural_response_map import NeuralResponseMap
```
Then you need to instantiate the class. For this you must pass the tensorflow model as a parameter

```python
nrm = NeuralResponseMap(model)
```

Next you need to train the mapper. This function calculates the correlation between the neurons and performs the dimensionality reduction for subsequent graphs. For this you must pass the inputs as a parameter. The inputs are sample input data of the neural network, for example if your network is a VGG16, the inputs are images of your dataset. Also, if you wish, you can pass the layers you want to view as a parameter. If you don't pass the layers as a parameter, the visualization will use all the layers of the model.

```python
nrm.TrainMap(inputs, model.layers[:2])
```

Finally you can visualize your neural response map. To perform the visualization you must call GenerateMap and pass as a parameter the input examples that you want to visualize. If you pass more than one example, the display will be the average of all the neural response maps of the input data.

```python
nrm.GenerateMap(inputs[1:2])
```

<p align="center">
    <img src="https://github.com/joancerretani/NeuralResponseMap/blob/main/examples/neuralmap2.png">
</p>

GenerateMap allows other optional parameters:

 - method: this parameter controls the display method which can be linear or nearest. The linear method performs a linear interpolation between the values of the neuron's activations. Nearest, on the other hand, does not perform interpolation. The nearest method is the default value.
 - cmap: it is the color map that you want to use, by default it is viridis. If you want to know other visualization maps visit the following [link](https://matplotlib.org/3.5.0/tutorials/colors/colormaps.html).
 - size: it is the size of the image. This value is a tuple with (5,5) by default.
 - file: is the name and type of file in which you want to save the image (for example 'map.png'). If no path is passed the image is not saved.
 
Alternatively after the TrainMap call, you can call CircleProjection. This will make the neural response map more circular in shape.

```python
nrm.CircleProjection()
```

```python
nrm.GenerateMap(inputs[1:2])
```

<p align="center">
    <img src="https://github.com/joancerretani/NeuralResponseMap/blob/main/examples/neuralmap3.png">
</p>

 ## Authors
---

This package has been developed by:

<a href="https://www.linkedin.com/in/joancerretani/" target="blank">Joan Alberto Cerretani</a>