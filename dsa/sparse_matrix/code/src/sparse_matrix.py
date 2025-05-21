"""
My sparse matrix homework for DSA class!
Name: Ibrahim Salami
Year: 2025
"""

# my own error type for when something goes wrong
class MatrixError(Exception):
    pass

class SparseMatrix:
    def __init__(self, rows_or_path, cols=None):
        # this function can either:
        # 1. make a new empty matrix if we give it rows and cols
        # 2. load a matrix from a file if we give it a file path
        if type(rows_or_path) == str:
            self.elements = {}  # using dictionary to save space!
            self._read_from_file(rows_or_path)
        else:
            # make sure rows and cols are valid numbers
            if type(rows_or_path) != int or type(cols) != int:
                raise MatrixError("Input has wrong format")
            if rows_or_path <= 0 or cols <= 0:
                raise MatrixError("Input has wrong format")
            
            self.rows = rows_or_path
            self.cols = cols
            self.elements = {}  # empty dictionary for matrix values

    def _read_from_file(self, file_path):
        # tries to read a matrix from a file
        try:
            f = open(file_path, 'r')
            
            # first two lines should be rows= and cols=
            rows_line = f.readline().strip()
            cols_line = f.readline().strip()
            
            # try to get the size of the matrix
            try:
                if rows_line.startswith("rows="):
                    self.rows = int(rows_line.split('=')[1])
                else:
                    self.rows = 1
                    
                if cols_line.startswith("cols="):
                    self.cols = int(cols_line.split('=')[1])
                else:
                    self.cols = 1
            except:
                self.rows = 1
                self.cols = 1
            
            # now read all the matrix values
            for line in f:
                line = line.strip()
                if not line:  # skip empty lines
                    continue
                
                try:
                    # clean up the line - remove brackets and split numbers
                    line = line.replace('(', '').replace(')', '')
                    line = line.replace('[', '').replace(']', '')
                    line = line.replace('{', '').replace('}', '')
                    
                    # split into row, col, value
                    parts = [x.strip() for x in line.split(',')]
                    if len(parts) != 3:
                        continue
                        
                    # try to make the numbers into integers
                    try:
                        row = int(float(parts[0]))  # this handles both normal numbers and decimals
                        col = int(float(parts[1]))
                        val = int(float(parts[2]))
                        
                        # only save if the position is inside the matrix
                        if 0 <= row < self.rows and 0 <= col < self.cols:
                            self.set_element(row, col, val)
                    except:
                        continue
                        
                except:
                    continue
                    
            f.close()
                
        except FileNotFoundError:
            # if we can't find the file, just make a tiny matrix
            self.rows = 1
            self.cols = 1
        except Exception:
            # if anything else goes wrong, make a tiny matrix
            self.rows = 1
            self.cols = 1

    def get_element(self, row, col):
        # get a value from the matrix
        # returns 0 if nothing is stored there (that's what sparse means!)
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise MatrixError(f"position ({row}, {col}) is outside matrix size")
        return self.elements.get((row, col), 0)

    def set_element(self, row, col, val):
        # put a value into the matrix
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise MatrixError(f"position ({row}, {col}) is outside matrix size")
        
        # only store non-zero values to save memory
        # if it's zero, remove it from dictionary if it's there
        if val != 0:
            self.elements[(row, col)] = val
        elif (row, col) in self.elements:
            del self.elements[(row, col)]

    def add(self, other):
        # add this matrix to another matrix
        if self.rows != other.rows or self.cols != other.cols:
            raise MatrixError("can't add matrices of different sizes")
        
        result = SparseMatrix(self.rows, self.cols)
        
        # first copy all elements from this matrix
        for (r, c), val in self.elements.items():
            result.set_element(r, c, val)
        
        # then add all elements from the other matrix
        for (r, c), val in other.elements.items():
            curr = result.get_element(r, c)
            result.set_element(r, c, curr + val)
        
        return result

    def subtract(self, other):
        # subtract another matrix from this one
        if self.rows != other.rows or self.cols != other.cols:
            raise MatrixError("can't subtract matrices of different sizes")
        
        result = SparseMatrix(self.rows, self.cols)
        
        # first copy all elements from this matrix
        for (r, c), val in self.elements.items():
            result.set_element(r, c, val)
        
        # then subtract all elements from the other matrix
        for (r, c), val in other.elements.items():
            curr = result.get_element(r, c)
            result.set_element(r, c, curr - val)
        
        return result

    def multiply(self, other):
        # multiply this matrix with another matrix
        if self.cols != other.rows:
            raise MatrixError("can't multiply - columns of first matrix must equal rows of second matrix")
        
        result = SparseMatrix(self.rows, other.cols)
        
        # make a helper dictionary for the second matrix
        # it groups elements by row to make multiplication faster
        helper = {}
        for (r, c), val in other.elements.items():
            if r not in helper:
                helper[r] = []
            helper[r].append((c, val))
        
        # go through each value in first matrix
        for (r1, c1), v1 in self.elements.items():
            # check if we have any matching values in second matrix
            if c1 in helper:
                # multiply matching values and add to result
                for c2, v2 in helper[c1]:
                    curr = result.get_element(r1, c2)
                    result.set_element(r1, c2, curr + v1 * v2)
        
        return result

    def save_to_file(self, file_path):
        # save the matrix to a file
        f = open(file_path, 'w')
        
        # write the size of the matrix
        f.write(f"rows={self.rows}\n")
        f.write(f"cols={self.cols}\n")
        
        # write all the non-zero values
        for (r, c), val in sorted(self.elements.items()):
            f.write(f"({r}, {c}, {val})\n")
            
        f.close() 