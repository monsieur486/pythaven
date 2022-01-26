#!/bin/bash

conda update --all
conda env export --no-builds | grep -v "prefix" > environment.yml