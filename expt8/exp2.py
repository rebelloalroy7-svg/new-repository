import numpy as np
# for inporting bash pip or pip3 install numpy
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Squared:", arr ** 2)

# next code 2
from scipy import integrate

# Integrate x^2 from 0 to 2
result, _ = integrate.quad(lambda x: x**2, 0, 2)
print("Integral of x^2 from 0 to 2:", result)

# next code 3
import tensorflow as tf

# Create a simple constant tensor
a = tf.constant([[1, 2], [3, 4]])
b = tf.constant([[5, 6], [7, 8]])
c = tf.matmul(a, b)

print("Matrix multiplication:\n", c.numpy())

# next code 4
import pandas as pd

data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# next code 5
import math

x = 16
print("Square root:", math.sqrt(x))
print("Sin(90 degrees):", math.sin(math.radians(90)))

# next code 6
import torch

# Create a tensor
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = x ** 2
y.backward(torch.tensor([1.0, 1.0, 1.0]))

print("Gradients:", x.grad)

# next code 7
import plotly.express as px

# Simple line chart
fig = px.line(x=[1, 2, 3], y=[10, 20, 15], title="Simple Line Chart")
fig.show()

# next code 8
from bs4 import BeautifulSoup

html = "<html><body><h1>Hello, world!</h1></body></html>"
soup = BeautifulSoup(html, "html.parser")

print("Text inside h1:", soup.h1.text)

# next code 9
from scapy.all import IP, ICMP, sr1

# Send a ping request (may require admin rights)
packet = IP(dst="8.8.8.8") / ICMP()
response = sr1(packet, timeout=1, verbose=0)

if response:
    print("Ping successful! Response from:", response.src)
else:
    print("No response.")

# next code

