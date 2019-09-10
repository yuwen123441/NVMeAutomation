
import os
from ctypes import c_uint8, c_uint16, c_uint32, c_uint64, Array, Union, Structure, CDLL
from ctypes import POINTER, cast, sizeof, addressof, memmove, memset, pointer


class Buffer(object):

    def __init__(self, length, buf_type):
        # self.dll = self.load_buffer_library()
        self.buf_length = length
        self.buf_type = buf_type
        self.buffer = self.new()

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

    def convert(self, types, index=0):
        """Cast buffer to type lp and return buf[index]"""
        return cast(self.buffer, POINTER(types))[index]

    def cast(self, types):
        """Cast buffer to type lp"""
        return cast(self.buffer, POINTER(types))