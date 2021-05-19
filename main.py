import copy


class Matrix:

    def __init__(self, inper):
        self.rows, self.columns = inper.split()

    def create(self):
        self.matrix = [[float(n) for n in input().split()] for _row in range(int(self.rows))]

    def add(self, mtx):
        if self.rows == mtx.rows and self.columns == mtx.columns:
            result = [[self.matrix[i][j] + mtx.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                      range(len(self.matrix))]
            for row in result:
                for number in row:
                    print(number, end=" ")
                print()
        else:
            print("ERROR")

    def multiply(self, number):
        result = [[self.matrix[i][j] * number for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        for row in result:
            for number in row:
                print(round(number, 4), end=" ")
            print()

    def transpose(self):
        transposed = [[self.matrix[i][j] for i in range(len(self.matrix))] for j in range(len(self.matrix[0]))]
        self.matrix = transposed

    def transpose_side(self):
        transposed = [[self.matrix[i][j] for i in range(-1, -len(self.matrix) - 1, -1)] for j in
                      range(-1, -len(self.matrix[0]) - 1, -1)]
        self.matrix = transposed

    def transpose_vertical(self):
        for row in self.matrix:
            row.reverse()

    def transpose_horizontal(self):
        self.matrix.reverse()

    def printer(self):
        for row in self.matrix:
            for number in row:
                print(int(number), end=" ")
            print()

    def multiply_matrices(self, mtx):
        if self.columns != mtx.rows:
            print("La operacion no se puede no realizar.")
        else:
            result = [[sum([self.matrix[i][k] * mtx.matrix[j][k] for k in range(len(mtx.matrix[0]))]) for j in
                       range(len(mtx.matrix))] for i in range(len(self.matrix))]

            for row in result:
                for number in row:
                    print(round(number, 2), end=" ")
                print()
                
    @staticmethod        
    def determinant(mtx):
        if len(mtx) == 1:
            return mtx[0][0]
        elif len(mtx) == 2:
            det = mtx[0][0] * mtx[1][1] - mtx[1][0] * mtx[0][1]
            return det
        else:
            recur = 0
            for i, e in enumerate(mtx):
                rex = mtx[0][i] * Matrix.determinant([[el for ind, el in enumerate(matx) if ind != i] for matx in mtx[1:]])
                if i % 2 == 0:
                    recur += rex
                else:
                    recur -= rex
            return recur
            
    @staticmethod
    def create_identity_matrix(siz):
        size = int(siz.split()[0])
        return [[1 if i == j else 0 for i in range(size)] for j in range(size)]
        
    @staticmethod
    def cofactor_matrix(size, mtx):
        cofa = []
        for i in range(len(mtx)):
            temp_cof = []
            for j in range(len(mtx[0])):
                temp_mtx = copy.deepcopy(mtx)
                temp_mtx.pop(i)
                # print(temp_mtx)
                for mitx in temp_mtx:
                    # print(mitx)
                    mitx.pop(j)
                    # print(mitx)
                cof_el = Matrix.determinant(temp_mtx) * (-1)**(i+j) 
                temp_cof.append(cof_el)   
            cofa.append(temp_cof)
        c = Matrix(size)
        c.matrix = cofa
        return c
                
            
def menu():
    while True:
        print("1. Sumar Matrices\n2. Multiplicar Matrices por una constante\n3. Multiplicar Matrices\n\
4. Matriz Transpuesta\n5. Calcular Determinante\n6. Matriz Inversa\n0. Exit")
        choice = input()
        if choice == "1":
            print("Ingresar Tamaño de la primera Matriz: ")
            matrix_a = Matrix(input())
            print("Ingresar Primera matriz: ")
            matrix_a.create()

            print("Ingresar Tamaño de la segunda Matriz: ")
            matrix_b = Matrix(input())
            print("Ingresar Segunda matriz: ")
            matrix_b.create()

            print("El resultado es:")
            matrix_a.add(matrix_b)

        elif choice == "2":
            print("Ingresar Tamaño de la Matriz: ")
            matrix_a = Matrix(input())
            print("Enter matrix: ")
            matrix_a.create()

            const = int(input("Enter constant: "))
            print("El resultado es:")
            matrix_a.multiply(const)

        elif choice == "3":
            print("Ingresar Tamaño de la primera Matriz: ")
            matrix_a = Matrix(input())
            print("Ingresar Primera matriz: ")
            matrix_a.create()

            print("Ingresar Tamaño de la segunda Matriz: ")
            matrix_b = Matrix(input())
            print("Ingresar Segunda matriz: ")
            matrix_b.create()
            matrix_b.transpose()
            # print(matrix_b.matrix)
            print("El resultado es:")
            matrix_a.multiply_matrices(matrix_b)

        elif choice == "4":
            print('1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line')
            tran_choice = input("Tu Eleccion: ")
            print("Ingresar Tamaño de la Matriz: ")
            matrix_a = Matrix(input())
            print("Enter matrix: ")
            matrix_a.create()
            if tran_choice == "1":
                matrix_a.transpose()
            elif tran_choice == "2":
                matrix_a.transpose_side()
            elif tran_choice == "3":
                matrix_a.transpose_vertical()
            elif tran_choice == "4":
                matrix_a.transpose_horizontal()

            matrix_a.printer()
            
        elif choice == "5":
            print("Ingresar Tamaño de la Matriz: ")
            matrix_a = Matrix(input())
            print("Enter matrix: ")
            matrix_a.create()
            print("El resultado es:")
            print(matrix_a.determinant(matrix_a.matrix))
        
        elif choice == "6":
            size = input("Ingresar Tamaño de la Matriz: ")
            matrix_a = Matrix(size)
            print("Enter matrix: ")
            matrix_a.create()
            det_a = matrix_a.determinant(matrix_a.matrix)
            
            iden = Matrix.create_identity_matrix(size)
            matrix_c = Matrix.cofactor_matrix(size, matrix_a.matrix)
            matrix_c.transpose()
            # print(matrix_c.matrix)
            # print(det_a)
            if det_a:
                print("El resultado es:")
                matrix_c.multiply(1 / det_a)
            else:
                print("Esta Matriz no tiene inversa.")
            
        else:
            break


menu()
