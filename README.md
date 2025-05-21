# Sparse Matrix Calculator

## What's in this Project?

Here's how my files are organized:
```
dsa/
└── sparse_matrix/
    ├── code/
    │   └── src/
    │       ├── sparse_matrix.py    # My main matrix code
    │       └── main.py            # Program that runs everything
    ├── sample_inputs/             # Example matrix files
    └── outputs/                   # Where results are saved
```

## What Does It Do?

My program can:
- Read matrices from files
- Do matrix math (add, subtract, multiply)
- Save results to files
- Handle big matrices without using too much memory
- Check for mistakes in input files

## How to Use It

1. Run the program:
```bash
cd dsa/sparse_matrix/code/src
python3 main.py
```

2. Follow the menu:
   - Pick an operation (1-4)
   - Type the paths to your input files
   - Enter a name for your output file (it'll be saved in the outputs folder)

## Input File Format

Your input files should look like this:
```
rows=3
cols=3
(0, 1, 5)
(1, 2, -3)
(2, 0, 4)
```

This means:
- First line: how many rows
- Second line: how many columns
- Then each line is (row, column, value)
- You don't need to write the zero values!

## How It Works

I used some cool tricks to make this work:
1. Used a dictionary to only store non-zero values (saves memory!)
2. Made a helper system to make multiplication faster
3. Added checks to make sure the matrices are the right size
4. Made it handle different kinds of input files

## Important Rules

When using matrices:
- For adding/subtracting: matrices must be the same size
- For multiplying: first matrix columns must equal second matrix rows
- All numbers must be whole numbers (no decimals!)
- Matrix positions start from 0 (like Python lists)

## What I Learned

This project taught me:
- How to work with sparse matrices
- Why saving memory is important
- How to handle files in Python
- How to make my code faster
- How to check for errors