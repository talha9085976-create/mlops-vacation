# MLOps Vacation: Foundations of Production ML

A hands-on engineering sandbox built inside WSL Ubuntu (Linux) to master high-performance data processing, environment isolation, and infrastructure tracking.

## 🚀 Key Milestones Achieved

### 1. Isolated Architecture
* Engineered a sandboxed development environment using Python's `venv` to bypass OS-level managed environment protections.
* Deployed package management workflows using `pip` inside an active terminal sub-shell.

### 2. High-Performance Vectorization Benchmark
* Developed a processing benchmark script (`vectorized_processor.py`) comparing standard Python logic to native C-accelerated compiled libraries.
* **Performance Result:** Vectorized calculations using NumPy processed 1,000,000 data points **266.3x faster** than traditional programmatic loops by leveraging SIMD parallelism.

## 📁 Repository Structure
* `math_processor.py`: Traditional programmatic data loops calculating base engineering metrics (Mean & Variance).
* `vectorized_processor.py`: High-speed matrix calculation script benchmarking NumPy execution speeds.

## 🛠️ How to Run Locally
1. Ensure you are on a Linux/WSL environment.
2. Activate the workspace sandbox:
```bash
   source .venv/bin/activate
   