import subprocess

# This is a short script that profiles the two versions of the spelling bee program
# found in the root directory. It uses python3's cProfiler utility to check the speed
# of the two implementations. The output is a table of methods with the time spent
# running each. The "-s cumtime" argument tells the profiler to sort the output by
# the cumulative time metric, which is accurate even for recursive methods. The
# subprocess call just runs the two programs through the profiler from the command line.

argv = ['python3', '-m', 'cProfile', '-s', 'cumtime']

subprocess.call(argv + ["spelling-bee-for-bench.py"])
subprocess.call(argv + ["spelling-bee-naive-for-bench.py"])
