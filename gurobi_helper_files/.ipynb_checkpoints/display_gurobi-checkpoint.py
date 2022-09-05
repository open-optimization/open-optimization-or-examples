#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 22:51:05 2020

@author: RobertH
"""

from IPython.display import display, Math, Latex
import numpy as np
from gurobipy import *
import array_to_latex as a2l

# converts constraint to a string
def con2str(constraint, model:Model):
    V = list(model.getVars())
    con = ''
    count = 0
    for v in V:
        coeff = model.getCoeff(constraint,v)
        if round(coeff) == coeff:
            coeff = int(coeff)
        if coeff > 0:
            if count > 0:
                con = con + '+'
            con = con + str(coeff) + v.VarName.replace('[','_{').replace(']','}')
            count = count + 1
        if coeff < 0:
            #if count > 0:
            con = con + '-'
            con = con + str(-coeff) + v.VarName.replace('[','_{').replace(']','}')
            count = count + 1
    
    b = constraint.rhs
    if b == round(b):
        b = int(b)
    if constraint.sense == '=':
        con = con + '&=' + str(b)
    if constraint.sense == '<':
        con = con + '&\leq ' + str(b)
    if constraint.sense == '>':
        con = con + '&\geq ' + str(b)
        
    return con
def obj2str(model :Model):
    V = list(model.getVars())
    con = ''
    count = 0
    for v in V:
        coeff = v.obj
        if round(coeff) == coeff:
            coeff = int(coeff)
        if coeff > 0:
            if count > 0:
                con = con + '+'
            con = con + str(coeff) + v.VarName.replace('[','_{').replace(']','}')
            count = count + 1
        if coeff < 0:
            #if count > 0:
            con = con + '-'
            con = con + str(-coeff) + v.VarName.replace('[','_{').replace(']','}')
            count = count + 1
        
    return con


def disp_model(model :Model, latex = False):
    cons = list(model.getConstrs())
    strModel = r'\textbf{' + model.ModelName + r'}\\ '
    if model.ModelSense == GRB.MAXIMIZE:
        strModel = strModel + r'\begin{array}{lrlr} \max & '
    if model.ModelSense == GRB.MINIMIZE:
        strModel = strModel + r'\begin{array}{lrlr} \min &  '

    strModel = strModel + obj2str(model) + r'\\'
    for c in cons:
        strModel = strModel + '&'+ con2str(c,model) + r'& \text{' +  c.ConstrName + '}' + r'\\'

    strModel = strModel + r'\end{array}'
    
    if latex:
        print(strModel)
        return strModel
    return Math(strModel)

def coeff_matrix(model:Model, latex = False, digits = 2, arraytype = 'pmatrix'):
    V = list(model.getVars())
    cons = list(model.getConstrs())
    A = np.array([[int(model.getCoeff(c,v)) for v in V] for c in cons])
    if latex:
        return a2l.to_ltx(coeff_matrix(model), frmt = '{:6.' + str(digits) + 'f}', arraytype = 'pmatrix')
    return A

def var_vector(model:Model,  arraytype = 'pmatrix'):
    V = list(model.getVars())
    varStr = r'\begin{' + arraytype + r'}'
    for v in V:
        varStr = varStr + v.VarName.replace('[','_{').replace(']','}') + r'\\ '

    varStr = varStr + r'\end{' + arraytype + r'}'
    return Math(varStr)  
    
