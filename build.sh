#!/bin/bash
cd liba
conan create . liba/0.1@
conan create . liba/1.0@
cd ..
cd libb
conan create .
cd ..
cd libc
conan create .
cd ..
cd libd
conan create . --build=missing
