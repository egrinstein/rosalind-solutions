#!/usr/bin env python
#! -*- coding: utf-8 -*-

def rabbit_count( month , rate , grown_rabbits , baby_rabbits ):
  if month == 0:
    return 0

  offspring  = grown_rabbits*rate

  grown_rabbits += baby_rabbits

  aux = baby_rabbits

  baby_rabbits = offspring

  return aux + rabbit_count( month - 1 , rate , grown_rabbits , baby_rabbits )

rabbit_count(28,2,0,1)



