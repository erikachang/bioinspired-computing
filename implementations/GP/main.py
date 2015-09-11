#!/usr/bin/env python
# coding=utf-8
'''explicacao do import:
      nome do arquivo  |  nome do que vai ser importado
            \/                      \/                  '''
from geneticProgram import GeneticProgramClass


if __name__ == "__main__": 
	aux = GeneticProgramClass()
	print aux.reproducao()
	print "FIM"
