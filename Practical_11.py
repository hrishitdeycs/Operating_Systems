# Memory Allocation Strategies: First-Fit, Best-Fit, Worst-Fit

# First-Fit Allocation
def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i, process in enumerate(processes):
        for j, block in enumerate(blocks):
            if block >= process:
                allocation[i] = j
                blocks[j] -= process
                break
    return allocation

# Best-Fit Allocation
def best_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i, process in enumerate(processes):
        best_idx = -1
        for j, block in enumerate(blocks):
            if block >= process:
                if best_idx == -1 or blocks[j] < blocks[best_idx]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            blocks[best_idx] -= process
    return allocation

# Worst-Fit Allocation
def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i, process in enumerate(processes):
        worst_idx = -1
        for j, block in enumerate(blocks):
            if block >= process:
                if worst_idx == -1 or blocks[j] > blocks[worst_idx]:
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            blocks[worst_idx] -= process
    return allocation

# Print allocation table
def print_allocation(allocation, processes):
    print("{:<12} {:<15} {:<15}".format("Process No.", "Process Size", "Block Allocated"))
    print("-" * 42)
    for i, block in enumerate(allocation):
        block_str = str(block + 1) if block != -1 else "Not Allocated"
        print("{:<12} {:<15} {:<15}".format(i + 1, processes[i], block_str))

# Main program
def main():
    memory_blocks = [100, 500, 200, 300, 600]
    processes = [212, 417, 112, 426]

    print("First-Fit Allocation:")
    first_fit_alloc = first_fit(memory_blocks.copy(), processes)
    print_allocation(first_fit_alloc, processes)

    print("\nBest-Fit Allocation:")
    best_fit_alloc = best_fit(memory_blocks.copy(), processes)
    print_allocation(best_fit_alloc, processes)

    print("\nWorst-Fit Allocation:")
    worst_fit_alloc = worst_fit(memory_blocks.copy(), processes)
    print_allocation(worst_fit_alloc, processes)

# Run the program
if __name__ == "__main__":
    main()
