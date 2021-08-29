#!/usr/bin/python3

# -*- coding: utf-8 -*-
""" Exercícios do Curso: Programação em Python do básico ao avançado

Curso da Udemy criado pela Geek University

Disponível no endereço:
https://www.udemy.com/course/curso-de-programacao-em-python-do-basico-ao-avancado

Exercícios da Seção 04

06. Leia uma temperatura em graus Celsius e apresenta-a convertida em graus Fahrenheit.
A fórmula de conversão é: F = C * (9.0 / 5.0) + 32.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius.

"""

__author__ = "Rafael Silva"
__version__ = "0.0.1"


def main():

    valor = input("Informe a temperatura em graus Celsius: ")

    celsius = float(valor)
    fahrenheit = celsius * 9.0 / 5.0 + 32.0

    print(f"A temperatura digitada corresponde a {fahrenheit} graus Fahrenheit")


if __name__ == "__main__":
    main()