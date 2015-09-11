#!/usr/bin/env python
# coding=utf-8

class GeneticProgramClass(object):
	#coloquei alguns atributos de exemplo que podem ser utilizados
	__tamanhoPopInicial          = None
	__percentualReproducaoDarwin = None
	__percentualCrossover        = None
	__percentualMutacao          = None
	__percentualPermutacao       = None
	__listaTerminais             = None
	__listaFuncoes               = None
	
	#construtor da classe
	def __init__(self):
		print "INIT"

	'''
	#### PSEUDO-CODIGO ######### TIRADO DOS SLIDES ####
	1. Definir a População Inicial
	2. Enquanto não chegar ao fitness X ou geração Y
		a. Avaliar Fitness da População
		b. Escolher os X indivíduos como Pais
		c. Realizar Operações Genéticas
	3. Retornar o melhor indivíduo(com o fitness X ou da geração Y)

	'''
	def pseudoCodigo(self):
		print "pseudoCodigo"


	'''
	#### REPRODUCAO ######### TIRADO DOS SLIDES ####
	1. Copiar T*E indivíduos para nova populacao (Elitismo)
	2. Enquanto tamanho(nova população) < T
		a. Executar Crossover com possibilidade C de sucesso
		b. Executar Mutação com possibilidade M de sucesso
		c. Adicionar novos indivíduos na nova populacao
	3. Retornar a população gerada
	'''
	def reproducao(self):
		print "reproducao"
		return
