#!/bin/bash
echo "[+] start build... "
i686-w64-mingw32-g++ -std=c++11 maldev.cpp -o maldev.exe -s -lws2_32 -Wno-write-strings -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc
echo "[+] end of the build "
