#!/usr/bin/env bash

gcc -fPIC -shared -o ../../nvme/nvme_library.so nvme-ioctl.c nvme-ioctl.h