from lk_heuristic.utils.solver_funcs import solve
from timeit import default_timer as timer
start = timer()
solve(tsp_file="Uruguay734.tsp", solution_method="lk1_improve", runs=50, logging_level=20)
end = timer()
print("Time: {}".format(end - start))
print("-----------------------------------------------------")
start = timer()
solve(tsp_file="Uruguay734.tsp", solution_method="lk2_improve", runs=25, logging_level=20)
end = timer()
print("Time: {}".format(end - start))