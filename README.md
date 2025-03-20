# biofasta-tools
Tools for biologists to convert FASTA files and analyze GC content
# BioFASTA Tools 🧬

## Quick Start
### Convert FASTA to CSV
```bash
git clone https://github.com/kelvinpeter/biofasta-tools
cd biofasta-tools
python fasta_to_csv.py --input sequences.fasta --output data.csv
## 🧬 Plot GC Content
Visualize GC% of sequences in a FASTA file.

### Usage
```bash
python gc_plot.py --fasta input.fasta --plot gc_plot.png
python gc_plot.py --fasta examples/sample.fasta --plot my_gc_plot.png
