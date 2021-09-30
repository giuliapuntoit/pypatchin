#!/bin/bash

echo "Hello world!"

for (( counter=10; counter>0; counter-- ))
do
echo -n "$counter "
done
printf "\n"
