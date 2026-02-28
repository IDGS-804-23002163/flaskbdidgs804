"""inicio del modulo de modelos"""
from flask import Blueprint

maestros=Blueprint('maestros',__name__,
                   template_folder='templates',
                   static_folder='static')
