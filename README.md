# img_compare (Lablaw Digitial SRE)
A simple click python cli that takes in a csv containing absolute paths 
of image pairs, and outputs a csv containing similarity scores for each pair.

## Get Started:
- Ensure you have python 3 installed.
- Run the following command to install requirements and setup the cli
  > `python3 -m pip install --editable .`
- Run `img_compare --help` to check options
- To update to a newer version just run ``python3 -m pip install --editable .`` again after pulling the latest upstream branch

Example usage:
>`img_compare --file ./data.csv --output ./output.csv`


## Design:
I chose to make this into a CLI in order to simplify the usage as much as possible and allow for further automation layers.
This was tested in both Windows and Mac OS environments just ensure to be mindful of file path structure
when using each system.