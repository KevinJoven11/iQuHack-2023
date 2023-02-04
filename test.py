import qiskit
from qiskit import quantum_info
from qiskit.execute_function import execute
from qiskit import BasicAer
import numpy as np
import pickle
import json
import os
import sys
from collections import Counter
from sklearn.metrics import mean_squared_error
from typing import Dict, List
import matplotlib.pyplot as plt

if len(sys.argv) > 1:
    data_path = sys.argv[1]
else:
    data_path = '.'

#define utility functions

def simulate(circuit: qiskit.QuantumCircuit) -> dict:
    """Simulate the circuit, give the state vector as the result."""
    backend = BasicAer.get_backend('statevector_simulator')
    job = execute(circuit, backend)
    result = job.result()
    state_vector = result.get_statevector()

    histogram = dict()
    for i in range(len(state_vector)):
        population = abs(state_vector[i]) ** 2
        if population > 1e-9:
            histogram[i] = population

    return histogram


def histogram_to_category(histogram):
    """This function takes a histogram representation of circuit execution results, and processes into labels as described in
    the problem description."""
    assert abs(sum(histogram.values())-1)<1e-8
    positive=0
    for key in histogram.keys():
        digits = bin(int(key))[2:].zfill(20)
        if digits[-1]=='0':
            positive+=histogram[key]

    return positive

def count_gates(circuit: qiskit.QuantumCircuit) -> Dict[int, int]:
    """Returns the number of gate operations with each number of qubits."""
    counter = Counter([len(gate[1]) for gate in circuit.data])
    #feel free to comment out the following two lines. But make sure you don't have k-qubit gates in your circuit
    #for k>2
    for i in range(2,20):
        assert counter[i]==0

    return counter


def image_mse(image1,image2):
    # Using sklearns mean squared error:
    # https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html
    return mean_squared_error(255*image1,255*image2)

def test():
    #load the actual hackthon data (fashion-mnist)
    images=np.load(data_path+'/images.npy')
    labels=np.load(data_path+'/labels.npy')

    #test part 1

    n=len(images)
    mse=0
    gatecount=0

    for image in images:
        #encode image into circuit
        circuit,image_re=run_part1(image)
        image_re = np.asarray(image_re)

        #count the number of 2qubit gates used
        gatecount+=count_gates(circuit)[2]

        #calculate mse
        mse+=image_mse(image,image_re)

    #fidelity of reconstruction
    f=1-mse/n
    gatecount=gatecount/n

    #score for part1
    score_part1=f*(0.999**gatecount)

    #test part 2

    score=0
    gatecount=0
    n=len(images)

    for i in range(n):
        #run part 2
        circuit,label=run_part2(images[i])

        #count the gate used in the circuit for score calculation
        gatecount+=count_gates(circuit)[2]

        #check label
        if label==labels[i]:
            score+=1
    #score
    score=score/n
    gatecount=gatecount/n

    score_part2=score*(0.999**gatecount)

    print(score_part1, ",", score_part2, ",", data_path, sep="")


############################
#      YOUR CODE HERE      #
############################
def encode(image):
    img_arr = np.asarray(downsizing_2(image)).reshape(-1)
    desired_state = img_arr
    q = qiskit.QuantumRegister(len(desired_state))
    circuit = qiskit.QuantumCircuit(q)
    i=0
    for ele in desired_state:
        if ele>1e-8:
            circuit.rx(10*ele,i)
        i+=1
    return circuit

def downsizing_2(sample_img):
    test_img = np.zeros((2,2))
    break_pt = [14,28]
    for i in range(2):
        for j in range(2):
            test_img[i,j] = round(np.mean(sample_img[14*i:break_pt[i],14*j:break_pt[j]]),5)
    return test_img

def reconstruction_2(test_img):
    img = np.zeros((28,28))
    min_img = 1e-4
    for i in range(14):
        for j in range(14):
            img[13-i,13-j] = max(round(test_img[0,0] - j*1e-5  - 2*min_img,5),0)

    for i in range(14):
        for j in range(14):
            img[13-i,13+j] = max(round(test_img[0,1]-2*min_img -j*1e-5 ,5),0)

    for i in range(14):
        for j in range(14):
            img[14+i,13- j]= max(round(test_img[1,0] - j**2*1e-5 - 0.5*i*1e-6 - 2*min_img,5),0)
    for i in range(14):
        for j in range(14):
            img[14+i,13+ j]= max(round(test_img[1,1] - j**2*1e-5 - 0.5*i*1e-6 - 2*min_img,5),0)

    return img
def decode(histogram):
    n=4
    options = {}
    hist_keys = list(histogram.keys())
    for i in range(n):
        options[i]=0
    for i in range(len(histogram)):
        for j in range(i,len(histogram)):
            x = hist_keys[i]^hist_keys[j]
            if x and (not(x & (x-1))):
                val1 = bin(hist_keys[i])[2:].zfill(n)
                val2 = bin(hist_keys[j])[2:].zfill(n)
                for k in range(n):
                    if val1[k]!=val2[k]:
                        if options[n-1-k] ==0:
                            options[n-1-k] = 2*np.arctan(np.sqrt(histogram[hist_keys[j]]/histogram[hist_keys[i]]))
            else:
                continue
    image = []
    for i in range(n):
        image.append(round(options[i]/10,4))
    return reconstruction_2(np.asarray(image).reshape((2,2)))

def run_part1(image):
    #encode image into a circuit
    circuit=encode(image)

    #simulate circuit
    histogram=simulate(circuit)

    #reconstruct the image
    image_re=decode(histogram)

    return circuit,image_re

def run_part2(image):
    # load the quantum classifier circuit
    classifier=qiskit.QuantumCircuit.from_qasm_file('quantum_classifier.qasm')

    #encode image into circuit
    circuit=encode(image)

    #append with classifier circuit
    nq1 = circuit.width()
    nq2 = classifier.width()
    nq = max(nq1, nq2)
    qc = qiskit.QuantumCircuit(nq)
    qc.append(circuit.to_instruction(), list(range(nq1)))
    qc.append(classifier.to_instruction(), list(range(nq2)))

    #simulate circuit
    histogram=simulate(qc)

    #convert histogram to category
    label=histogram_to_category(histogram)

    #thresholding the label, any way you want
    if label>0.5:
        label=1
    else:
        label=0

    return circuit,label

############################
#      END YOUR CODE       #
############################

test()
