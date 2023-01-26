# iQuHack-2023

To-Do:

1. Learn Python (All)
2. Learn Qbraid (All)
3. Insert Block diagram (Onri)
4. Learn IonQ ProjectQ & Azure Quantum resources (All)

## Block Diagram

![image](https://user-images.githubusercontent.com/75779966/213802274-d79860c5-3e51-444c-840c-79cdca29bcf1.png)

Azure Quantum Resources 
[Create an Azure Quantum workspace - Azure Quantum | Microsoft Docs](https://learn.microsoft.com/en-us/azure/quantum/how-to-create-workspace?tabs=payg%2Ctabid-quick)

[ Get started with Q# and an Azure Quantum notebook - Azure Quantum | Microsoft Docs ](https://learn.microsoft.com/en-us/azure/quantum/get-started-jupyter-notebook?tabs=tabid-ionq)

[ Submit Qiskit quantum circuits to Azure Quantum using an online notebook - Azure Quantum | Microsoft Docs ](https://learn.microsoft.com/en-us/azure/quantum/quickstart-microsoft-qiskit-portal?pivots=platform-ionq)

[Azure Quantum job costs - Azure Quantum | Microsoft Docs](https://learn.microsoft.com/en-us/azure/quantum/azure-quantum-job-costs)

[How to bulk add users to an Azure Quantum workspace - Azure Quantum | Microsoft Docs](https://learn.microsoft.com/en-us/azure/quantum/bulk-add-users-to-a-workspace)

Here are a few docs related to optimization:

 

[Submit optimization jobs to Azure Quantum - Azure Quantum | Microsoft Docs](https://learn.microsoft.com/en-us/azure/quantum/how-to-submit-jobs-optimization?pivots=ide-portal)

[Introduction to optimization - Azure Quantum | Microsoft Docs](https://learn.microsoft.com/en-us/azure/quantum/optimization-overview-introduction)

[Publish a QIO job as an Azure Function - Azure Quantum | Microsoft Docs](https://learn.microsoft.com/en-us/azure/quantum/how-to-publish-qio-job-as-azurefunction)

[microsoft/qio-samples: Samples for using optimization solvers through Azure Quantum. (github.com)](https://github.com/microsoft/qio-samples)

[List of optimization targets on Azure Quantum - Azure Quantum | Microsoft Docs](https://learn.microsoft.com/en-us/azure/quantum/qio-target-list)

## Papers we can implement or discuss interesting papers on Error correction, optimization, Chemistry using trapped ions

[Realization of Real-Time Fault-Tolerant Quantum Error Correction](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.11.041058) Error correction Very Important

[Quantum error correction with metastable states of trapped ions using erasure conversion](https://arxiv.org/abs/2210.15024)

[Quantum Error correction important](https://pubmed.ncbi.nlm.nih.gov/34608286/)

[Error correction very important](https://pubmed.ncbi.nlm.nih.gov/35614250/)

[Topological Trapped ion](https://www.science.org/doi/abs/10.1126/science.1253742)

[qec](https://arxiv.org/pdf/0809.4368.pdf)

[qec](https://arxiv.org/pdf/0809.4368)

[Constrained quantum optimization for extractive summarization](https://www.nature.com/articles/s41598-022-20853-w)

[Optimizing electronic structure simulations on a trapped-ion quantum computer using problem decomposition](https://www.nature.com/articles/s42005-021-00751-9)

[opti](https://www.pnas.org/doi/10.1073/pnas.2006373117)

[maxcut](https://scai.engineering.asu.edu/2021-22-seminars/trapped-ion-quantum-computing-and-quantum-approximate-optimization-algorithm-for-maxcut-problem/)

[QAOA ](https://inspirehep.net/literature/2021742)

[Adiabatic quantum optimization](https://www.frontiersin.org/articles/10.3389/fphy.2015.00021/full)

ml(https://uwspace.uwaterloo.ca/handle/10012/17322)

ml(https://scholar.google.co.in/scholar?q=Machine+Learning+and+Optimization.+Techniques+for+Trapped-ion+Quantum.+Simulators&hl=en&as_sdt=0&as_vis=1&oi=scholart)

ieee(https://ieeexplore.ieee.org/document/9860175/)

[Digital-Analog Quantum Simulation of Spin Models in Trapped Ions ](https://www.nature.com/articles/srep30534)

[Digital Quantum Simulation of the Schwinger Model and Symmetry Protection with Trapped Ions (Journal Article) | DOE PAGES](https://www.osti.gov/pages/biblio/1866519)

[ionq](https://ionq.com/resources/publications)

[Quantum Chemistry Calculations on a Trapped-Ion Quantum Simulator](https://arxiv.org/abs/1803.10238)

[Crosstalk Suppression for Fault-tolerant Quantum Error Correction with Trapped Ions](https://quantum-journal.org/papers/q-2021-06-29-487/)

[error correction paper ](https://physicstoday.scitation.org/doi/10.1063/1.1897514)

[error correction](http://qserver.usc.edu/qec11/slides/Blatt_QEC11.pdf)

## Tutorials and resources New Updated Tutorials 

https://inspirehep.net/literature/1964622 paper on Quantum machine learning

https://github.com/PennyLaneAI/pennylane-aqt

https://ionq.com/docs/get-started-with-qiskit IonQ Qiskit Tutorials 

https://pennylane.ai/qml/demos/tutorial_trapped_ions.html

https://github.com/PennyLaneAI/qml/blob/master/demonstrations/tutorial_trapped_ions.py

https://www.nature.com/articles/s41534-021-00456-5

[resource on error correction] (https://abdullahkhalid.com/qecft/)

## Challenges in Trapped ion quantum according to this paper https://arxiv.org/pdf/0809.4368.pdf

In order to achieve universal quantum computing, the algorithms have to
be implemented in a fault-tolerant way. It is commonly accepted that this
requires quantum error correction. Therefore, currently one of the most important goals is to implement quantum error correction repeatedly with high
fidelity to prolong coherence times and to correct for errors induced by the
gate operations. The largest obstacle to perform a successful quantum error
correction protocol seems to be the limited fidelity of the operations. The current state of the art for the control in ion trap quantum computing can be
summarized as follows:
• The qubit coherence times are one or two orders of magnitude longer than
the basic (gate) operations. In specific cases coherence times longer by more
than five orders of magnitude the gate time are available (see Sec. 3.1.2).
In most current experiments, motional decoherence is not a problem. In
addition, it can be further suppressed with cooling of the trap electrodes
(see Sec. 3.2).
• Initialization accuracies are on the order of 0.999 as discussed in Sec. 2.4.
Most likely they can be improved further if necessary.
• Single qubit operation can be carried out with fidelities exceeding 0.995
(Knill et al., 2008). If required, further improvements are possible with more
stable laser fields at the ion positions.
• Implementations of two-qubit gate operations achieve fidelities of about 0.9–
0.99. Depending on the gate type, various sources limit the fidelity. Errors
are caused by off-resonant scattering, imperfect addressing of individual

