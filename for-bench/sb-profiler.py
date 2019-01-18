import subprocess

argv = ['python', '-m', 'cProfile', '-s', 'cumtime']

subprocess.call(argv + ["spelling-bee-for-bench.py"])
subprocess.call(argv + ["spelling-bee-naive-for-bench.py"])
