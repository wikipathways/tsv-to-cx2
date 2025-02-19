# tsv-to-cx2
## How to use?
This Python script converts a TSV (Tab-Separated Values) file containing gene node information into a Cytoscape CX2 JSON file. The output file retains full node table information and follows the CX2 format used by Cytoscape and Cytoscape Web.

 **Run the Script:**  
   Open a terminal (or command prompt) and run the script using Python:
   ```bash
   python converter.py
   ```
When prompted, type in the name of your TSV file (including the .tsv extension), then press Enter.

The script will process the TSV file and create a new file with the same base name as the input but with a .cx2 extension. For example, if your input file is myData.tsv, the output will be myData.cx2.

## Where to get tsv file?
https://pfocr.wikipathways.org
