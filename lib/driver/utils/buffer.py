
import os
import sys
from ctypes import c_uint8, c_uint16, c_uint32, c_uint64, Array, Union, Structure, CDLL
from ctypes import POINTER, cast, sizeof, addressof, memmove, memset, pointer


class Buffer(object):

    def __init__(self, length, buf_type):
        # self.dll = self.load_buffer_library()
        self.buf_length = length
        self.buf_type = buf_type
        self.buffer = self.new()
        self.m_sizeof = sizeof(self.buf_type)
        self.m_size = self.buf_length * self.m_sizeof

    @property
    def length(self):
        return self.buf_length

    def load_buffer_library(self):
        so_path = os.path.realpath(os.path.join(os.path.dirname(__file__), "buf.so"))
        return CDLL(so_path)

    def get_buffer(self):
        return self.buffer

    def new(self):
        return (self.buf_type * self.buf_length)()

    def delete(self):
        pass

    def set(self, types, index, value):
        if not 0 <= index < self.m_size // sizeof(types):
            raise RuntimeError("[ERR] out of range(types: {}, index: {})".format(types, index))
        cast(self.buffer, POINTER(types))[index] = value

    def set_uint8(self, offset, value):
        self.set(c_uint8, offset, value)

    def convert(self, types, index=0):
        """Cast buffer to type lp and return buf[index]"""
        return cast(self.buffer, POINTER(types))[index]

    def cast(self, types):
        """Cast buffer to type lp"""
        return cast(self.buffer, POINTER(types))

    def memcopy(self, stream, offset=0, length=sys.maxsize):
        """Set buffer by stream"""
        data = [ord(i) for i in list(stream)]
        size = min(length, len(data), self.m_size)
        for i in range(size):
            self.set_uint8(offset + i, data[i])