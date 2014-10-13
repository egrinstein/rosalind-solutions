#!/usr/bin env python
#! -*- coding: utf-8 -*-



def count_rabbits(month,mortality):
  total = [1,1]
  newborns = [1,0]
  i = 2
  while i < month:
    litter = total[i-1] - newborns[i-1]
    index = i - mortality
    deaths = 0
    if index >= 0:
      deaths = newborns[index]
    curr =  litter - deaths + total[i-1]
    total.append(curr)
    newborns.append(litter)
    i+=1
    print total
    print newborns
  return total[i-1]


count_rabbits(89,20)
