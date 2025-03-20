import argparse
from Bio import SeqIO

def fasta_to_csv(input_file, output_file):
    with open(input_file, "r") as fasta, open(output_file, "w") as csv:
        csv.write("header,sequence,length\n")
        for record in SeqIO.parse(fasta, "fasta"):
            csv.write(f"{record.id},{str(record.seq)},{len(record)}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert FASTA to CSV')
    parser.add_argument('--input', required=True, help='Input FASTA file')
    parser.add_argument('--output', required=True, help='Output CSV file')
    args = parser.parse_args()
    fasta_to_csv(args.input, args.output)
