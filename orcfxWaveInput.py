#!/usr/bin/env python
import math as math

if __name__ == "__main__":
  f1 = open('BaseCase.yml','r')
  for h in range(3,7):
    for t in range (5, 13):
      ratio = t/math.sqrt(h)
      if ratio<= 3.6:
        gamma = 5
      elif ratio >= 5:
        gamma = 1
      else:
        gamma = math.exp(5.75-1.15*ratio)

      with open('H{}m_T{}s.yml'.format(h,t),'w') as f2:
        for lineA in f1:
          lineA.replace("WaveHs: 3","WaveHs: {}".format(h)) # WaveHs: 3 indicates the ex. Basecase Hs
          lineA.replace("WaveTz: 2.84184","WaveTp: {}".format(t)) # WaveTp: 3 indicates the ex. Basecase Tp, want to use Tp instead of zero-cross
          lineA.replace("WaveGamma: 1","WaveGamma: {}".format(gamma)) # WavePeriod: 3 indicates the ex. Basecase gamma
          f2.write(lineA)
        f2.close()
      f1.seek(0)
  f1.close()
