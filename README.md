# Learning-to-Design-Application-Aware-Approximate-Multipliers
Tools: Python, PyTorch, NSGA-II, PPO, MOEA/D, Cadence Virtuoso


Developed an AI-driven framework for design space exploration of approximate 8-bit Baugh–Wooley multipliers using 22 configurable compressor variants.

Integrated multi-objective optimization algorithms (NSGA-II, PPO, MOEA/D) to minimize power, latency, and power-delay product (PDP) while preserving inference accuracy in neural networks (LeNet-5 and MLP).

Leveraged TorchApprox for NN simulation and Cadence Virtuoso for hardware characterization of compressors.

Achieved designs with up to 200× reduction in power and latency and maintained >90% accuracy using fine-grained compressor mixing.

