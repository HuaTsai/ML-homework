import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
  global fin, fin2
  fin = pd.read_csv("train.csv")
  fin2 = pd.read_csv("test.csv")

if __name__ == '__main__':
  main()
