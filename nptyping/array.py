"""
The array module: support for typing Numpy ndarrays.
"""
import functools
import numpy as np
from nptyping import _array_meta


class Array(metaclass=_array_meta.meta()):
    """
    A representation of the `numpy.ndarray`.

    Example of an array with an undefined generic type and shape:
        `Array`

    Example of an array with a defined generic type:
        `Array[int]`

    Example of an array with a defined generic type and shape (rows):
        `Array[int, 3]`
        `Array[int, 3, ...]`
        `Array[int, 3, None]`

    Examples of an array with a defined generic type and shape (cols):
        `Array[int, None, 2]`
        `Array[int, ..., 2]`

    Example of an array with a defined generic type and shape (rows and cols):
        `Array[int, 3, 2]`

    """
    @functools.wraps(np.ndarray.__abs__)
    def __abs__(self): ...

    @functools.wraps(np.ndarray.__add__)
    def __add__(self): ...

    @functools.wraps(np.ndarray.__and__)
    def __and__(self): ...

    @functools.wraps(np.ndarray.__array__)
    def __array__(self): ...

    @functools.wraps(np.ndarray.__array_finalize__)
    def __array_finalize__(self): ...

    @functools.wraps(np.ndarray.__array_function__)
    def __array_function__(self): ...

    @functools.wraps(np.ndarray.__array_interface__)
    def __array_interface__(self): ...

    @functools.wraps(np.ndarray.__array_prepare__)
    def __array_prepare__(self): ...

    @functools.wraps(np.ndarray.__array_priority__)
    def __array_priority__(self): ...

    @functools.wraps(np.ndarray.__array_struct__)
    def __array_struct__(self): ...

    @functools.wraps(np.ndarray.__array_ufunc__)
    def __array_ufunc__(self): ...

    @functools.wraps(np.ndarray.__array_wrap__)
    def __array_wrap__(self): ...

    @functools.wraps(np.ndarray.__bool__)
    def __bool__(self): ...

    @functools.wraps(np.ndarray.__complex__)
    def __complex__(self): ...

    @functools.wraps(np.ndarray.__contains__)
    def __contains__(self): ...

    @functools.wraps(np.ndarray.__copy__)
    def __copy__(self): ...

    @functools.wraps(np.ndarray.__deepcopy__)
    def __deepcopy__(self): ...

    @functools.wraps(np.ndarray.__delitem__)
    def __delitem__(self): ...

    @functools.wraps(np.ndarray.__divmod__)
    def __divmod__(self): ...

    @functools.wraps(np.ndarray.__float__)
    def __float__(self): ...

    @functools.wraps(np.ndarray.__floordiv__)
    def __floordiv__(self): ...

    @functools.wraps(np.ndarray.__getitem__)
    def __getitem__(self): ...

    @functools.wraps(np.ndarray.__iadd__)
    def __iadd__(self): ...

    @functools.wraps(np.ndarray.__iand__)
    def __iand__(self): ...

    @functools.wraps(np.ndarray.__ifloordiv__)
    def __ifloordiv__(self): ...

    @functools.wraps(np.ndarray.__ilshift__)
    def __ilshift__(self): ...

    @functools.wraps(np.ndarray.__imatmul__)
    def __imatmul__(self): ...

    @functools.wraps(np.ndarray.__imod__)
    def __imod__(self): ...

    @functools.wraps(np.ndarray.__imul__)
    def __imul__(self): ...

    @functools.wraps(np.ndarray.__index__)
    def __index__(self): ...

    @functools.wraps(np.ndarray.__int__)
    def __int__(self): ...

    @functools.wraps(np.ndarray.__invert__)
    def __invert__(self): ...

    @functools.wraps(np.ndarray.__ior__)
    def __ior__(self): ...

    @functools.wraps(np.ndarray.__ipow__)
    def __ipow__(self): ...

    @functools.wraps(np.ndarray.__irshift__)
    def __irshift__(self): ...

    @functools.wraps(np.ndarray.__isub__)
    def __isub__(self): ...

    @functools.wraps(np.ndarray.__iter__)
    def __iter__(self): ...

    @functools.wraps(np.ndarray.__itruediv__)
    def __itruediv__(self): ...

    @functools.wraps(np.ndarray.__ixor__)
    def __ixor__(self): ...

    @functools.wraps(np.ndarray.__len__)
    def __len__(self): ...

    @functools.wraps(np.ndarray.__lshift__)
    def __lshift__(self): ...

    @functools.wraps(np.ndarray.__matmul__)
    def __matmul__(self): ...

    @functools.wraps(np.ndarray.__mod__)
    def __mod__(self): ...

    @functools.wraps(np.ndarray.__mul__)
    def __mul__(self): ...

    @functools.wraps(np.ndarray.__neg__)
    def __neg__(self): ...

    @functools.wraps(np.ndarray.__or__)
    def __or__(self): ...

    @functools.wraps(np.ndarray.__pos__)
    def __pos__(self): ...

    @functools.wraps(np.ndarray.__pow__)
    def __pow__(self): ...

    @functools.wraps(np.ndarray.__radd__)
    def __radd__(self): ...

    @functools.wraps(np.ndarray.__rand__)
    def __rand__(self): ...

    @functools.wraps(np.ndarray.__rdivmod__)
    def __rdivmod__(self): ...

    @functools.wraps(np.ndarray.__rfloordiv__)
    def __rfloordiv__(self): ...

    @functools.wraps(np.ndarray.__rlshift__)
    def __rlshift__(self): ...

    @functools.wraps(np.ndarray.__rmatmul__)
    def __rmatmul__(self): ...

    @functools.wraps(np.ndarray.__rmod__)
    def __rmod__(self): ...

    @functools.wraps(np.ndarray.__rmul__)
    def __rmul__(self): ...

    @functools.wraps(np.ndarray.__ror__)
    def __ror__(self): ...

    @functools.wraps(np.ndarray.__rpow__)
    def __rpow__(self): ...

    @functools.wraps(np.ndarray.__rrshift__)
    def __rrshift__(self): ...

    @functools.wraps(np.ndarray.__rshift__)
    def __rshift__(self): ...

    @functools.wraps(np.ndarray.__rsub__)
    def __rsub__(self): ...

    @functools.wraps(np.ndarray.__rtruediv__)
    def __rtruediv__(self): ...

    @functools.wraps(np.ndarray.__rxor__)
    def __rxor__(self): ...

    @functools.wraps(np.ndarray.__setitem__)
    def __setitem__(self): ...

    @functools.wraps(np.ndarray.__setstate__)
    def __setstate__(self): ...

    @functools.wraps(np.ndarray.__sub__)
    def __sub__(self): ...

    @functools.wraps(np.ndarray.__truediv__)
    def __truediv__(self): ...

    @functools.wraps(np.ndarray.__xor__)
    def __xor__(self): ...

    @functools.wraps(np.ndarray.all)
    def all(self): ...

    @functools.wraps(np.ndarray.any)
    def any(self): ...

    @functools.wraps(np.ndarray.argmax)
    def argmax(self): ...

    @functools.wraps(np.ndarray.argmin)
    def argmin(self): ...

    @functools.wraps(np.ndarray.argpartition)
    def argpartition(self): ...

    @functools.wraps(np.ndarray.argsort)
    def argsort(self): ...

    @functools.wraps(np.ndarray.astype)
    def astype(self): ...

    @functools.wraps(np.ndarray.base)
    def base(self): ...

    @functools.wraps(np.ndarray.byteswap)
    def byteswap(self): ...

    @functools.wraps(np.ndarray.choose)
    def choose(self): ...

    @functools.wraps(np.ndarray.clip)
    def clip(self): ...

    @functools.wraps(np.ndarray.compress)
    def compress(self): ...

    @functools.wraps(np.ndarray.conj)
    def conj(self): ...

    @functools.wraps(np.ndarray.conjugate)
    def conjugate(self): ...

    @functools.wraps(np.ndarray.copy)
    def copy(self): ...

    @functools.wraps(np.ndarray.ctypes)
    def ctypes(self): ...

    @functools.wraps(np.ndarray.cumprod)
    def cumprod(self): ...

    @functools.wraps(np.ndarray.cumsum)
    def cumsum(self): ...

    @functools.wraps(np.ndarray.data)
    def data(self): ...

    @functools.wraps(np.ndarray.diagonal)
    def diagonal(self): ...

    @functools.wraps(np.ndarray.dot)
    def dot(self): ...

    @functools.wraps(np.ndarray.dtype)
    def dtype(self): ...

    @functools.wraps(np.ndarray.dump)
    def dump(self): ...

    @functools.wraps(np.ndarray.dumps)
    def dumps(self): ...

    @functools.wraps(np.ndarray.fill)
    def fill(self): ...

    @functools.wraps(np.ndarray.flags)
    def flags(self): ...

    @functools.wraps(np.ndarray.flat)
    def flat(self): ...

    @functools.wraps(np.ndarray.flatten)
    def flatten(self): ...

    @functools.wraps(np.ndarray.getfield)
    def getfield(self): ...

    @functools.wraps(np.ndarray.imag)
    def imag(self): ...

    @functools.wraps(np.ndarray.item)
    def item(self): ...

    @functools.wraps(np.ndarray.itemset)
    def itemset(self): ...

    @functools.wraps(np.ndarray.itemsize)
    def itemsize(self): ...

    @functools.wraps(np.ndarray.max)
    def max(self): ...

    @functools.wraps(np.ndarray.mean)
    def mean(self): ...

    @functools.wraps(np.ndarray.min)
    def min(self): ...

    @functools.wraps(np.ndarray.nbytes)
    def nbytes(self): ...

    @functools.wraps(np.ndarray.ndim)
    def ndim(self): ...

    @functools.wraps(np.ndarray.newbyteorder)
    def newbyteorder(self): ...

    @functools.wraps(np.ndarray.nonzero)
    def nonzero(self): ...

    @functools.wraps(np.ndarray.partition)
    def partition(self): ...

    @functools.wraps(np.ndarray.prod)
    def prod(self): ...

    @functools.wraps(np.ndarray.ptp)
    def ptp(self): ...

    @functools.wraps(np.ndarray.put)
    def put(self): ...

    @functools.wraps(np.ndarray.ravel)
    def ravel(self): ...

    @functools.wraps(np.ndarray.real)
    def real(self): ...

    @functools.wraps(np.ndarray.repeat)
    def repeat(self): ...

    @functools.wraps(np.ndarray.reshape)
    def reshape(self): ...

    @functools.wraps(np.ndarray.resize)
    def resize(self): ...

    @functools.wraps(np.ndarray.round)
    def round(self): ...

    @functools.wraps(np.ndarray.searchsorted)
    def searchsorted(self): ...

    @functools.wraps(np.ndarray.setfield)
    def setfield(self): ...

    @functools.wraps(np.ndarray.setflags)
    def setflags(self): ...

    @functools.wraps(np.ndarray.shape)
    def shape(self): ...

    @functools.wraps(np.ndarray.size)
    def size(self): ...

    @functools.wraps(np.ndarray.sort)
    def sort(self): ...

    @functools.wraps(np.ndarray.squeeze)
    def squeeze(self): ...

    @functools.wraps(np.ndarray.std)
    def std(self): ...

    @functools.wraps(np.ndarray.strides)
    def strides(self): ...

    @functools.wraps(np.ndarray.sum)
    def sum(self): ...

    @functools.wraps(np.ndarray.swapaxes)
    def swapaxes(self): ...

    @functools.wraps(np.ndarray.take)
    def take(self): ...

    @functools.wraps(np.ndarray.tobytes)
    def tobytes(self): ...

    @functools.wraps(np.ndarray.tofile)
    def tofile(self): ...

    @functools.wraps(np.ndarray.tolist)
    def tolist(self): ...

    @functools.wraps(np.ndarray.tostring)
    def tostring(self): ...

    @functools.wraps(np.ndarray.trace)
    def trace(self): ...

    @functools.wraps(np.ndarray.transpose)
    def transpose(self): ...

    @functools.wraps(np.ndarray.var)
    def var(self): ...

    @functools.wraps(np.ndarray.view)
    def view(self): ...
