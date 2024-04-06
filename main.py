import matplotlib.pyplot as plt
import collections

def file_read(file_path):
     with open(file_path, 'r') as file:
        file_sizes = [int(line.strip()) for line in file]
        return file_sizes

file_sizes = file_read('file.txt')

def analyze_file_sizes(file_sizes):
    total_files = len(file_sizes)
    average_size = sum(file_sizes) / total_files
    smallest_size = min(file_sizes)
    largest_size = max(file_sizes)
    file_sizes_sorted = sorted(file_sizes)
    median_size = file_sizes_sorted[total_files // 2] if total_files % 2 != 0 else \
                  (file_sizes_sorted[total_files // 2 - 1] + file_sizes_sorted[total_files // 2]) / 2

    size_ranges = collections.defaultdict(int)
    detailed_size_ranges = collections.defaultdict(int)

    for size in file_sizes:
        # Broad categorization
        if size < 10**4:
            size_ranges['1KB-10KB'] += 1
        elif size < 10**5:
            size_ranges['10KB-100KB'] += 1
        elif size < 10**6:
            size_ranges['100KB-1MB'] += 1
        elif size < 10**7:
            size_ranges['1MB-10MB'] += 1
        elif size < 10**9:
            size_ranges['10MB-1GB'] += 1
        else:
            size_ranges['1GB+'] += 1

        # Detailed categorization
        if size < 10**4:
            detailed_size = f"{size // 1000}KB"
            detailed_size = "<1KB" if detailed_size == "0KB" else detailed_size
            detailed_size_ranges[detailed_size] += 1
        elif size < 10**5:
            detailed_size_ranges['100KB'] += 1
        elif size < 10**6:
            detailed_size_ranges['100KB-1MB'] += 1
        elif size < 10**7:
            detailed_size_ranges['1MB-10MB'] += 1
        elif size < 10**9:
            detailed_size_ranges['10MB-1GB'] += 1
        else:
            detailed_size_ranges['1GB+'] += 1

    print(f"Total files: {total_files}")
    print(f"Average file size: {average_size} bytes")
    print(f"Smallest file size: {smallest_size} bytes")
    print(f"Largest file size: {largest_size} bytes")
    print(f"Median file size: {median_size} bytes")
    print("Broad Distribution of file sizes:")


    size_ranges = dict(sorted(size_ranges.items(), key=lambda k_v: k_v[1], reverse=True))
    detailed_size_ranges = dict(sorted(detailed_size_ranges.items(), key=lambda k_v: k_v[1], reverse=True))
    for range, count in size_ranges.items():
        print(f"  {range}: {count} - {count/total_files * 100:.2f}%")

    print("-"*30)
    print("Detailed Distribution of file sizes:")
    for range, count in detailed_size_ranges.items():
        print(f"  {range}: {count} - {count/total_files * 100:.2f}%")

    return size_ranges, detailed_size_ranges

size_ranges, detailed_size_ranges = analyze_file_sizes(file_sizes)

def draw_histogram(file_counts):
    labels = list(file_counts.keys())
    counts = list(file_counts.values())
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, counts, color='red')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval:,}', ha='center', va='bottom')

    plt.title('File Size Distribution')
    plt.xlabel('File Size Range')
    plt.ylabel('Number of Files')
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis='y', linestyle='--', linewidth=0.7)
    plt.tight_layout()

    plt.show()

size_ranges, detailed_size_ranges

draw_histogram(size_ranges)

draw_histogram(detailed_size_ranges)