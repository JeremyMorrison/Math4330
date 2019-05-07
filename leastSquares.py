def LeastSquares(x,y):
  """Solve for degree 4 interpolating polynomial

  Build a degree 4 vandermonde matrix A, then use Mod G.S. to compute QR factorization of A, Next compute the inverse of Q, and use back substitution to solve Rb=Q^*y, and finally use b for coefficients of degree 4 interpolating polynomial.

  Args:
    Two complex vectors x and y 
  Returns:
    A degree 4 interpolating polynomail
  """


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

Qz=ConjugateTranspose(Q):

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

v=dot(Qz,y):
B=BackSub(R,v):

def d4Interpolate(B,x):
"""performs polynomial interpolation

Multiply the elements of B by x raised to the corresponding exponent to get a dgree 4 interpolating polynomail.

Args:
  a vector B whcih we get from BackSub function
Returns:
  a degree 4 interpolating polynomial
"""
return(B[0]+B[1]*x+B[2]*(x**2)+B[3]*(x**3)+B[4]*(x**4))