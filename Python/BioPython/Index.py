bioinformatics_topics = {
    "1. Python Fundamentals": [
        "Data types (lists, tuples, dictionaries, sets)",
        "Loops and conditionals (for, while, if-else)",
        "Functions and modules",
        "File handling (reading/writing CSV, FASTA, etc.)"
    ],
    "2. Scientific Computing & Data Handling": [
        "NumPy: For handling large numerical datasets efficiently.",
        "Pandas: Data manipulation and analysis, useful for processing genomic datasets.",
        "Matplotlib & Seaborn: Data visualization for bioinformatics results."
    ],
    "3. Bioinformatics-Specific Libraries": [
        "Biopython: Handling sequence data (FASTA, GenBank), BLAST searches, and parsing biological databases.",
        "Scipy & Statsmodels: Statistical analysis of biological data.",
        "Scikit-learn: Machine learning for genomic and proteomic analysis."
    ],
    "4. Genomic Data Processing": [
        "Working with FASTA, FASTQ, and GenBank files.",
        "Analyzing Next-Generation Sequencing (NGS) data.",
        "Using PyVCF to handle Variant Call Format (VCF) files for genetic variations."
    ],
    "5. Structural Bioinformatics": [
        "MDAnalysis or PyMOL for molecular dynamics and protein structure analysis."
    ],
    "6. Bioinformatics Algorithms": [
        "Sequence alignment (global and local alignment).",
        "Phylogenetic tree construction (using Biopython or ETE Toolkit).",
        "Hidden Markov Models (HMM) for gene prediction."
    ],
    "7. Automation & Scripting": [
        "Writing Python scripts to automate repetitive bioinformatics tasks.",
        "Using regular expressions (re module) to extract patterns from DNA/protein sequences."
    ],
    "8. Data Science & Machine Learning Applications": [
        "Feature selection for biological datasets.",
        "Clustering and classification of gene expression data.",
        "Deep learning applications in genomics (using TensorFlow/PyTorch)."
    ]
}

for category, topics in bioinformatics_topics.items():
    print(f"{category}")
    for topic in topics:
        print(f"  - {topic}")
    print("\n")