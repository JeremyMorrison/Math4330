def TwoNorm(vector):
  """computes the 2-norm of a vector

  Takes the elements of a vector and adds the squares of the absolute values and then returns the sqare root of the sum.

  Args:
    vector: a list of real and complex numbers
  Returns:
    a scalar representing the 2-norm of a vector
  """
  result=0
  for element in range(len(vector)):
    result=result+(vector[element].real)**2+(vector[element].imag)**2
  result=result**(1/2)
  return result

def scalarVectorMulti(scalar,vector):
  """computes scalar vector multiplication

  Takes a scalar and multiplies it by the elements of a vactor.

  Args:
    scalar: a real number
    vector: a list of real and complex numbers
  Returns:
    A vector reoresenting scalar vector multiplication
  """
  result=vector
  for element in range(len(result)):
    result[element]=scalar*result[element]
  return result

def normalize(vector):
  """Normalizes a vector

  Checks to see if input is valid and either displays error or normalizes the vector using scalar vector multiplication.

  Args:
    vector: a list of real and complex numbers
  Returns:
    a normalized vector
  """
  norm=TwoNorm(vector)
  if (norm !=0):
    return scalarVectorMulti((1/norm,vector))
  else:
    print("invalid input")

def vectorAddition(vector_1,vector_2):
  """Computes vector addition

  Takes two vectors and adds them together to form one vector.

  Args:
    Two vectors which are lists of real and complex numbers
  Returns:
    A vector representing vector addition of two vectors
  """
  result=vector_1
  for element in range(len(result)):
    result[element]=result[element]+vector_2[element]
  return result

def dot(vector01,vector02):
  """Compute dot product

  Takes two vectors and computes their dot product

  Args:
    vector01: a list of real numbers representing a vector01
    vector02: a list of real numbers with same dimensions as vector01 also representing a     vector01

  returns: 
    the dot product of the inputs
  """
  result = 0
  for iterator in range(len(vector01)):
    result=result + vector01[iterator]*vector02[iterator]
  return result

def complexConjugate(scalar):
  """Computes the complex conjugate of a scalar

  Takes a complex number and changes the sign to get its conjugate.

  Args:
    A scalar
  Retrns:
    The complex conjugate of the scalar
  """
  result=0
  result=+scalar.real
  result=result-(scalar.imag)*1j
  return result

def conjugateVector(vector):
  """Computes the conjugate of a vector

  Takes a vector and uses complex conjugate function to compute conjugate of a vector.

  Args:
    A vetor of real and complex numbers
  Return:
    The conjugate of a vector
  """
  result=[0]*len(vector)
  for element in range(len(vector)):
    result[element]=complexConjugate(vector[element])
  return result

def vandermonde(x):
  """Builds a vandermonde matrix of degree 4

  Build a matrix by appending elements of a vector x with the corresponding exponent to get an nxn vandermonde matrix of degree 4

  Args:
    A vector which is a list of real and complex numbers
  Return:
    A degree 4 vandermonde matrix
  """
  result=[]
  for exponent in range(5)
    temp=[]
    for element in range(len(x))
      temp.append(x[element]**exponent)
    result.append(temp)
  return result

def transpose(A):
  """Transposes matrix A

  Takes a matrix A and switches the columns and rows to get the transpose.

  Args:
    A matrix A
  Returns:
    The transpose of matrix A
  """
  result=[]
  for iterator = 0 to (len(A[0])-1)
    temp=[]
    for element = 0 to (len(A)-1)
      temp.append(A[iterator][element])
    result.append(temp)
  return result

def conjugateTranspose(A):
  """Computes conjugate transpose of matrix A

  We transpose matrix A then for the elements in A and then compute the conjugate using conjugate function to get the conjugate transpose of A.

  Args:
    A matrix A
  Returns:
    The conjugate transpose of matrix A
  """
  result=transpose(A):
  for iterator = 0 to (len(A)-1)
    for element = 0 to (len(A[0])-1)
      result[iterator][element]=complexConjugate(result[iterator][element])
  return result

def MS(S):
  """computes the sum of elements

  Starting at 0 and then adds the next element to the sum of the previous elements until termination.

  Args:
    A list of numbers
  Returns: 
    The sum of all the elements in a list
  """
  result=0
  for iterator = 1 to (len(s))
    result=result+S[iterator]
  return result

def BackSub(A,b):
  """Performes back substitution

  Perform back substitution to solve Ax=b

  Args:
    A matrix A and a vevctor b
  Returns:
    A scalar v that solves Av=b
  """
  result=b
  for iterator in range(len(A[0]))
    v=(len(A[0]-1))
    result[v-iterator]=(b[v-iterator]-MS(A[v-iterator][k]*result[k]))*(1/A[v-iterator][v-iterator])
  return result

def d4Interpolate(B,x)
"""performs polynomial interpolation

Multiply the elements of B by x raised to the corresponding exponent to get a dgree 4 interpolating polynomail.

Args:
  a vector B whcih we get from BackSub function
Returns:
  a degree 4 interpolating polynomial
"""
return(B[0]+B[1]*x+B[2]*(x**2)+B[3]*(x**3)+B[4]*(x**4))

def ModGS(A):
  """Using Mod GS to compute QR factorization of A

  Orthofonal decomposition and normalization such that A=QR

  Args:
    an mxn matrix A
  Returns:
    Unitary matrix Q and an uppertriangular matrix R
  """
  for j=1 to n
    V[j]=a[j]
  for j=1 to n
    r[j,j]=TwoNorm(v[j])
    q[j]=v[j]/r[j,j]
    for k=j+1 to n
      r[j,k]=dot(ConjugatTranspose(q[j]),v[k])
      v[k]=v[k]-dot(r[j,k],q[j])
  return [Q,R]