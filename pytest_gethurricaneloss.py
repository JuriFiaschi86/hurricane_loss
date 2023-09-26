import pytest
import subprocess


benchmark_valid = {
    "florida_landfall_rate": 3,
    "florida_mean": 5,
    "florida_stddev": 2,
    "gulf_landfall_rate": 2,
    "gulf_mean": 3,
    "gulf_stddev": 1,
    "num_monte_carlo_samples": 100000, # default MonteCarlo samples for test 10^6
    "mean_loss": 3358.05540 # from MonteCarlo samples 10^9 numba simulation
}

tolerance = 1e-1
#tolerance = 1e-3

def command_to_run(benchmark, script):
    return "python3 " + script + " " + str(benchmark["florida_landfall_rate"]) + " " + str(benchmark["florida_mean"]) + " " + str(benchmark["florida_stddev"]) + " " + str(benchmark["gulf_landfall_rate"]) + " " + str(benchmark["gulf_mean"]) + " " + str(benchmark["gulf_stddev"]) + " -n " + str(benchmark["num_monte_carlo_samples"])


#########################
### TEST NUMPY SCRIPT ###
#########################

script = "gethurricaneloss.py"

### Test valid input. Check result and tolerance
def test_numpy_valid():
    command = command_to_run(benchmark_valid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    output_test = float((out.split())[4])
    print(output_test)
    assert "Mean annual loss:" in out
    assert pytest.approx(output_test, rel=tolerance) == benchmark_valid["mean_loss"]

### Test invalid negative entries in Florida
def test_numpy_invalid_input_florida_landfall_rate():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["florida_landfall_rate"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "florida_landfall_rate must be >= 0. Exit." in out

def test_numpy_invalid_input_florida_mean():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["florida_mean"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "florida_mean must be >= 0. Exit." in out

def test_numpy_invalid_input_florida_stddev():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["florida_stddev"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "florida_stddev must be >= 0. Exit." in out

### Test invalid negative entries in Gulf states
def test_numpy_invalid_input_gulf_landfall_rate():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["gulf_landfall_rate"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "gulf_landfall_rate must be >= 0. Exit." in out

def test_numpy_invalid_input_gulf_mean():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["gulf_mean"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "gulf_mean must be >= 0. Exit." in out

def test_numpy_invalid_input_gulf_stddev():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["gulf_stddev"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "gulf_stddev must be >= 0. Exit." in out

### Test invalid negative entries in num_monte_carlo_samples
def test_numpy_invalid_input_num_monte_carlo_samples_integer():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["num_monte_carlo_samples"] = 0.5
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
    _, err = process.communicate()
    assert "error: argument -n/--num_monte_carlo_samples:" in err

def test_numpy_invalid_input_num_monte_carlo_samples_positive():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["num_monte_carlo_samples"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "florida_landfall_rate must be an integer > 0. Exit." in out






############################
### TEST MULTCORE SCRIPT ###
############################

script = "gethurricaneloss_multicores.py"

### Test valid input. Check result and tolerance
def test_multicore_valid():
    command = command_to_run(benchmark_valid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    output_test = float((out.split())[4])
    print(output_test)
    assert "Mean annual loss:" in out
    assert pytest.approx(output_test, rel=tolerance) == benchmark_valid["mean_loss"]

### Test invalid negative entries in Florida
def test_multicore_invalid_input_florida_landfall_rate():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["florida_landfall_rate"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "florida_landfall_rate must be >= 0. Exit." in out

def test_multicore_invalid_input_florida_mean():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["florida_mean"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "florida_mean must be >= 0. Exit." in out

def test_multicore_invalid_input_florida_stddev():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["florida_stddev"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "florida_stddev must be >= 0. Exit." in out

### Test invalid negative entries in Gulf states
def test_multicore_invalid_input_gulf_landfall_rate():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["gulf_landfall_rate"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "gulf_landfall_rate must be >= 0. Exit." in out

def test_multicore_invalid_input_gulf_mean():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["gulf_mean"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "gulf_mean must be >= 0. Exit." in out

def test_multicore_invalid_input_gulf_stddev():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["gulf_stddev"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "gulf_stddev must be >= 0. Exit." in out

### Test invalid negative entries in num_monte_carlo_samples
def test_multicore_invalid_input_num_monte_carlo_samples_integer():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["num_monte_carlo_samples"] = 0.5
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
    _, err = process.communicate()
    assert "error: argument -n/--num_monte_carlo_samples:" in err

def test_multicore_invalid_input_num_monte_carlo_samples_positive():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["num_monte_carlo_samples"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "florida_landfall_rate must be an integer > 0. Exit." in out




#########################
### TEST NUMBA SCRIPT ###
#########################

script = "gethurricaneloss_numba.py"

### Test valid input. Check result and tolerance
def test_numba_valid():
    command = command_to_run(benchmark_valid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    output_test = float((out.split())[4])
    print(output_test)
    assert "Mean annual loss:" in out
    assert pytest.approx(output_test, rel=tolerance) == benchmark_valid["mean_loss"]

### Test invalid negative entries in Florida
def test_numba_invalid_input_florida_landfall_rate():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["florida_landfall_rate"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "florida_landfall_rate must be >= 0. Exit." in out

def test_numba_invalid_input_florida_mean():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["florida_mean"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "florida_mean must be >= 0. Exit." in out

def test_numba_invalid_input_florida_stddev():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["florida_stddev"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "florida_stddev must be >= 0. Exit." in out

### Test invalid negative entries in Gulf states
def test_numba_invalid_input_gulf_landfall_rate():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["gulf_landfall_rate"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "gulf_landfall_rate must be >= 0. Exit." in out

def test_numba_invalid_input_gulf_mean():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["gulf_mean"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "gulf_mean must be >= 0. Exit." in out

def test_numba_invalid_input_gulf_stddev():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["gulf_stddev"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "gulf_stddev must be >= 0. Exit." in out

### Test invalid negative entries in num_monte_carlo_samples
def test_numba_invalid_input_num_monte_carlo_samples_integer():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["num_monte_carlo_samples"] = 0.5
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
    _, err = process.communicate()
    assert "error: argument -n/--num_monte_carlo_samples:" in err

def test_numba_invalid_input_num_monte_carlo_samples_positive():
    benchmark_invalid = benchmark_valid.copy()
    benchmark_invalid["num_monte_carlo_samples"] = -1
    command = command_to_run(benchmark_invalid, script)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    out, _ = process.communicate()
    assert "florida_landfall_rate must be an integer > 0. Exit." in out
