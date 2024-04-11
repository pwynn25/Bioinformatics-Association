import os
import re
import random
import string


def generate_random_directory():
    # Generate a random directory name with 6 characters
    directory_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return directory_name

def create_directory_with_file():
    # Generate a random directory name
    directory_name = generate_random_directory()
    # Create the directory
    os.makedirs(directory_name, exist_ok=True)
    # Create the consensi.fa.classified file inside the directory
    with open(os.path.join(directory_name, "consensi.fa.classified"), "w") as f:
        f.write("Sample content for consensi.fa.classified file")
    return directory_name


def replace_directory_in_script_output(script_output, random_directory):
    # Define the pattern to match the directory path
    pattern = r"Using output directory = .*"
    # Replace the directory path with the random directory name
    replaced_output = re.sub(pattern, f"Using output directory = {random_directory}", script_output)
    return replaced_output

def write_variable_to_file(variable):
    # Open the file in write mode
    with open("randomSlurm.out", "w") as file:
        # Write the content of the variable to the file
        file.write(str(variable))

# Sample Slurm script output
script_output = """
Restoring modules from user's default
Saved current collection of modules to: "default"

Restoring modules from user's default
Lmod Warning: The following modules were not loaded: defaultenv




You can now run `module load "sproul-mamba"` after restarting your shell
Building database sample.db:
  Reading /home/pw264/fsl_groups/grp_sproul_lab/compute/Patrick/testing/pipeline_testing/onecontig_test_JSS.bp.p_ctg_oneline.fasta...
Number of sequences (bp) added to database: 1 ( 409893 bp )
RepeatModeler Version 2.0.5
===========================
Using output directory = /nobackup/scratch/grp/grp_sproul_lab/Patrick/testing/pipeline_testing/onecontig_test_JSS_2024-04-05/RM_13290.FriApr51856532024
Search Engine = rmblast 2.14.1+
Threads = 24
Dependencies: TRF 4.09, RECON , RepeatScout 1.0.6, RepeatMasker 4.1.5
LTR Structural Analysis: Disabled [use -LTRStruct to enable]
Random Number Seed: 1712365013
Database = /nobackup/scratch/grp/grp_sproul_lab/Patrick/testing/pipeline_testing/onecontig_test_JSS_2024-04-05/sample.db
  - Sequences = 1
  - Bases = 409893
Storage Throughput = fair ( 449.93 MB/s )

Ready to start the sampling process.
INFO: The runtime of RepeatModeler heavily depends on the quality of the assembly
      and the repetitive content of the sequences.  It is not imperative
      that RepeatModeler completes all rounds in order to obtain useful
      results.  At the completion of each round, the files ( consensi.fa, and
      families.stk ) found in:
      /nobackup/scratch/grp/grp_sproul_lab/Patrick/testing/pipeline_testing/onecontig_test_JSS_2024-04-05/RM_13290.FriApr51856532024/
      will contain all results produced thus far. These files may be
      manually copied and run through RepeatClassifier should the program
      be terminated early.


RepeatModeler Round # 1
========================
Searching for Repeats
 -- Sampling from the database...
   - Gathering up to 40000000 bp
   - Final Sample Size = 409826 bp ( 409826 non ambiguous )
   - Num Contigs Represented = 1
   - Sequence extraction : 00:00:00 (hh:mm:ss) Elapsed Time
 -- Running RepeatScout on the sequences...
   - RepeatScout: Running build_lmer_table ( l = 11 )..
   - RepeatScout: Running RepeatScout.. : 16 raw families identified
   - RepeatScout: Running filtering stage.. 12 families remaining
   - RepeatScout: 00:00:15 (hh:mm:ss) Elapsed Time
   - Large Satellite Filtering.. : 0 found in 00:00:01 (hh:mm:ss) Elapsed Time
   - Collecting repeat instances...: 00:00:00 (hh:mm:ss) Elapsed Time
Refinement: 00:00:07 (hh:mm:ss) Elapsed Time
Family Refinement: 00:00:07 (hh:mm:ss) Elapsed Time
Round Time: 00:00:23 (hh:mm:ss) Elapsed Time : 3 families discovered.


RepeatModeler Round # 2
========================
Searching for Repeats
 -- Sampling from the database...
   - Gathering up to 10000000 bp
   - Sequence extraction : 00:00:00 (hh:mm:ss) Elapsed Time
 -- Running TRFMask on the sequence...
       72 Tandem Repeats Masked
   - TRFMask time 00:00:18 (hh:mm:ss) Elapsed Time
 -- Masking repeats from the previous rounds...
    -- Collecting 52 ranges...
       52 repeats masked totaling 14480 bp(s).
   - TE Masking time 00:00:00 (hh:mm:ss) Elapsed Time
 -- Sample Stats:
       Sample Size 409826 bp
       Num Contigs Represented = 1
       Non ambiguous bp:
             Initial: 409826 bp
             After Masking: 26040 bp
             Masked: 93.65 %
 -- Input Database Coverage: 409826 bp out of 409893 bp ( 99.98 % )
Sampling Time: 00:00:18 (hh:mm:ss) Elapsed Time
Running all-by-other comparisons...
  - Total Comparisons = 55
       18% completed,  00:0:04 (hh:mm:ss) est. time remaining.
       34% completed,  00:0:01 (hh:mm:ss) est. time remaining.
       49% completed,  00:0:01 (hh:mm:ss) est. time remaining.
       61% completed,  00:0:01 (hh:mm:ss) est. time remaining.
       72% completed,  00:0:00 (hh:mm:ss) est. time remaining.
       81% completed,  00:0:00 (hh:mm:ss) est. time remaining.
       89% completed,  00:0:00 (hh:mm:ss) est. time remaining.
       94% completed,  00:0:00 (hh:mm:ss) est. time remaining.
       98% completed,  00:0:00 (hh:mm:ss) est. time remaining.
      100% completed,  00:0:00 (hh:mm:ss) est. time remaining.
Comparison Time: 00:00:03 (hh:mm:ss) Elapsed Time, 78 HSPs Collected
  - RECON: Running imagespread..
RECON Elapsed: 00:00:01 (hh:mm:ss) Elapsed Time
  - RECON: Running initial definition of elements ( eledef )..
RECON Elapsed: 00:00:00 (hh:mm:ss) Elapsed Time
  - RECON: Running re-definition of elements ( eleredef )..
RECON Elapsed: 00:00:00 (hh:mm:ss) Elapsed Time
  - RECON: Running re-definition of edges ( edgeredef )..
RECON Elapsed: 00:00:00 (hh:mm:ss) Elapsed Time
  - RECON: Running family definition ( famdef )..
RECON Elapsed: 00:00:00 (hh:mm:ss) Elapsed Time
  - Obtaining element sequences
Number of families returned by RECON: 7
Processing families with greater than 15 elements
Instance Gathering: 00:00:00 (hh:mm:ss) Elapsed Time
Refining 0 families
Family Refinement: 00:00:00 (hh:mm:ss) Elapsed Time
Round Time: 00:00:22 (hh:mm:ss) Elapsed Time : 0 families discovered.

RepeatScout/RECON discovery complete: 3 families found


RepeatClassifier Version 2.0.5
======================================
  - Looking for Simple and Low Complexity sequences..
  - Looking for similarity to known repeat proteins..
  - Looking for similarity to known repeat consensi..
Classification Time: 00:00:15 (hh:mm:ss) Elapsed Time


Program Time: 00:01:00 (hh:mm:ss) Elapsed Time
Working directory:  /nobackup/scratch/grp/grp_sproul_lab/Patrick/testing/pipeline_testing/onecontig_test_JSS_2024-04-05/RM_13290.FriApr51856532024
may be deleted unless there were problems with the run.

The results have been saved to:
  /nobackup/scratch/grp/grp_sproul_lab/Patrick/testing/pipeline_testing/onecontig_test_JSS_2024-04-05/sample.db-families.fa  - Consensus sequences for each family identified.
  /nobackup/scratch/grp/grp_sproul_lab/Patrick/testing/pipeline_testing/onecontig_test_JSS_2024-04-05/sample.db-families.stk - Seed alignments for each family identified.
  /nobackup/scratch/grp/grp_sproul_lab/Patrick/testing/pipeline_testing/onecontig_test_JSS_2024-04-05/sample.db-rmod.log     - Execution log.  Useful for reproducing results.

The RepeatModeler stockholm file is formatted so that it can
easily be submitted to the Dfam database.  Please consider contributing
curated families to this open database and be a part of this growing
community resource.  For more information contact help@dfam.org.
"""

# Generate a random directory name

# this will create a random directory and the file we want then return the random directory
random_directory = create_directory_with_file()
print(random_directory)
# Replace the directory path in the script output
updated_output = replace_directory_in_script_output(script_output, random_directory)

# Create a file with the updated output
write_variable_to_file(updated_output)