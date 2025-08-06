import numpy as np
import csv
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.core.problem import Problem
from pymoo.operators.sampling.lhs import LHS
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
from moo import multi_objective_function
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.operators.sampling.lhs import LHS
from pymoo.operators.crossover.sbx import SimulatedBinaryCrossover
from pymoo.operators.mutation.pm import PM
from pymoo.operators.repair.rounding import RoundingRepair

# CSV file for logging inputs and outputs
log_file = "optimization_log_lat_acc.csv"

# Write the header to the log file
with open(log_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Input_Config"] + ["MRED", "Latency", "Power", "Accuracy"])

# Define the multi-objective problem
class MultiObjectiveOptimization(Problem):
    def __init__(self):
        super().__init__(
            n_var=20,  # Number of decision variables
            n_obj=2,   # Number of objectives (Power, Accuracy)
            # n_constr=0,  # No constraints
            xl=np.zeros(20),  # Lower bounds for decision variables
            xu=np.full(20, 21)  # Upper bounds for decision variables
        )

    def _evaluate(self, x, out, *args, **kwargs):
        results = []
        rows_to_log = []
        for xi in x:
            # Ensure xi is an integer (in case rounding wasn't applied elsewhere)
            xi = np.round(xi).astype(int)
            print(f"Processing input: {xi}")  # Debugging
            error, latency, power, accuracy = multi_objective_function(xi)
            rows_to_log.append([xi.tolist(), error, latency, power, accuracy])
            results.append([latency, -accuracy])  # Accuracy negated for minimization
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows_to_log)
        out["F"] = np.array(results)

# Define the NSGA-II algorithm
algorithm = NSGA2(
    pop_size=200,  # Larger population size for large search space
    sampling=LHS(),  # Latin Hypercube Sampling for better diversity
    crossover=SimulatedBinaryCrossover(prob=0.9, eta=15),  # SBX with crossover probability
    mutation=PM(prob=0.2, eta=3.0, vtype=float, repair=RoundingRepair()),  # Polynomial mutation
)

# Instantiate the problem
problem = MultiObjectiveOptimization()

# Run the optimization
res = minimize(
    problem,
    algorithm,
    termination=("n_gen", 200),  # Increase generations for better convergence
    seed=42,
    save_history=True,
    verbose=True,
)

# Visualize the Pareto front
plot = Scatter(title="Pareto Front (Lat vs. Accuracy)")
plot.add(res.F, facecolor="red", edgecolor="k")
plot.save("pareto_front_lat_acc.png")

# Extract Pareto-optimal solutions
pareto_solutions = res.X
pareto_objectives = res.F

print("Pareto-optimal solutions:")
for i, (solution, objectives) in enumerate(zip(pareto_solutions, pareto_objectives)):
    print(f"Solution {i + 1}: {solution}")
    print(f"Power: {objectives[0]}, Accuracy: {-objectives[1]}")  # Accuracy is negated back
