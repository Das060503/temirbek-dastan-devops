#!/bin/bash

echo "=============================="
echo "Student Information"
echo "=============================="
echo "Name: Dastan"
echo "Surname: Temirbek"
echo "Group: IT2-2308"
echo "Student ID: 37621"

echo
echo "=============================="
echo "System Information"
echo "=============================="

echo "Username: $(whoami)"
echo "Hostname: $(hostname)"
echo "Current Date: $(date)"
echo "Operating System: $(uname -s)"
echo
echo "Disk Usage:"
df -h /
echo
echo "Memory Usage:"
free -h

echo
if [ -f "Temirbek_Dastan_info.txt" ]; then
    echo "Student information file exists."
else
    echo "Student information file does not exist."
fi
