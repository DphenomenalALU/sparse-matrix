"""
This is the main program for running matrix operations
Name: Ibrahim Salami
Year: 2025
"""

from sparse_matrix import SparseMatrix, MatrixError
import os

def show_menu():
    print("\nSparse Matrix Calculator")
    print("------------------------")
    print("Select operation:")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction") 
    print("3. Matrix Multiplication")
    print("4. Exit")
    print("\nEnter choice (1-4): ")

def get_files():
    # Get the absolute path to sample_inputs directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sample_dir = os.path.abspath(os.path.join(current_dir, "../../sample_inputs"))
    
    print("\nInput File Format:")
    print("rows=<number>")
    print("cols=<number>")
    print("(row, col, value)")
    print("\nExample files are in:")
    print(sample_dir)
    print("\nAvailable sample files:")
    try:
        for file in os.listdir(sample_dir):
            if file.endswith('.txt'):
                print(f"- {file}")
    except:
        print("(No sample files found)")
    print()
    
    file1 = input("Enter first matrix file path: ").strip()
    file2 = input("Enter second matrix file path: ").strip()
    
    # Convert to absolute paths if relative paths are given
    if not os.path.isabs(file1):
        file1 = os.path.abspath(os.path.join(current_dir, file1))
    if not os.path.isabs(file2):
        file2 = os.path.abspath(os.path.join(current_dir, file2))
        
    return file1, file2

def save_matrix(result):
    # Get the absolute path to outputs directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    outputs_dir = os.path.abspath(os.path.join(current_dir, "../../outputs"))
    
    # Create outputs directory if it doesn't exist
    os.makedirs(outputs_dir, exist_ok=True)
    
    print("\nEnter output file name (will be saved in outputs folder):")
    out_name = input("File name: ").strip()
    
    # Add .txt extension if not provided
    if not out_name.lower().endswith('.txt'):
        out_name += '.txt'
    
    # Create full path in outputs directory
    out_file = os.path.join(outputs_dir, out_name)
    
    result.save_to_file(out_file)
    print(f"\nResult matrix saved to: {out_file}")
    print(f"Matrix dimensions: {result.rows} x {result.cols}")

def main():
    print("Sparse Matrix Calculator")
    print("Data Structures and Algorithms")
    print("Student: Ibrahim Salami")
    
    while True:
        try:
            show_menu()
            choice = input().strip()
            
            if choice == '4':
                print("\nExiting program...")
                break
                
            if choice not in ['1', '2', '3']:
                print("Invalid choice. Please select 1-4")
                continue
                
            # Get input files
            file1, file2 = get_files()
            
            try:
                # Load matrices
                print("\nLoading matrices...")
                matrix1 = SparseMatrix(file1)
                print(f"First matrix loaded: {matrix1.rows} x {matrix1.cols}")
                matrix2 = SparseMatrix(file2)
                print(f"Second matrix loaded: {matrix2.rows} x {matrix2.cols}")
                
                # Perform operation
                print("\nPerforming operation...")
                if choice == '1':
                    result = matrix1.add(matrix2)
                    print("Addition completed successfully")
                elif choice == '2':
                    result = matrix1.subtract(matrix2)
                    print("Subtraction completed successfully")
                else:  # choice == '3'
                    result = matrix1.multiply(matrix2)
                    print("Multiplication completed successfully")
                
                # Save result
                save_matrix(result)
                
            except MatrixError as e:
                print(f"\nError: {str(e)}")
                print("Please check input files and try again")
            except Exception as e:
                print(f"\nError: Input file has wrong format")
                
        except KeyboardInterrupt:
            print("\nOperation cancelled by user")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main() 