import argparse
from Bio import SeqIO
import matplotlib.pyplot as plt

def plot_gc_content(fasta_file, output_plot):
    lengths = []
    gc_percent = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = str(record.seq).upper()
        gc = (seq.count('G') + seq.count('C')) / len(seq) * 100
        gc_percent.append(gc)
        lengths.append(len(seq))

    plt.figure()
    plt.scatter(lengths, gc_percent, alpha=0.5)
    plt.xlabel('Sequence Length')
    plt.ylabel('GC Content (%)')
    plt.title('GC Content vs. Sequence Length')
    plt.savefig(output_plot)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot GC content of FASTA sequences')
    parser.add_argument('--fasta', required=True, help='Input FASTA file')
    parser.add_argument('--plot', required=True, help='Output plot file (e.g., plot.png)')
    args = parser.parse_args()
    plot_gc_content(args.fasta, args.plot)
