## uniq

I built a python based clone of uniq, a Linux command line utility.

### Usage

1. Input file outputs to stdout
   `python uniq.py input.txt`

2. Input file outputs to output file
   `python uniq.py input.txt output.txt`

3. stdin outputs to stdout
   `cat input.txt | python uniq.py`

4. stdin outputs to output file
   `cat input.txt | python uniq.py - output.txt`

5. Input file outputs to stdout (count included)
   `python uniq.py -c input.txt`

6. Input file outputs to stdout (repeated only)
   `python uniq.py -d input.txt`

7. Input file outputs to stdout (non-repeated only)
   `python uniq.py -u input.txt`
