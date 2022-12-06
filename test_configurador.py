#!/usr/bin/python3


"""
    Test de la Classe Configurador de la llista de la compra
"""
import unittest
import sys, os, shutil
sys.path.append("../Public_llista_compra_m06/")
from Configurador import Configurador
from Persistencia_factory import Persistencia_factory
from Persistencia_factory_mySql import Persistencia_factory_mySql


class SimpleTestCase(unittest.TestCase):

    def setUp(self):
        """ Es crida abans de cada test """
        # Set configuracio_mysql.yml as config file
        shutil.copyfile(
            os.path.join(
                os.path.dirname(__file__), 
                "configuracio_mysql.yml"
                ),
            os.path.join(
                os.path.dirname(__file__), 
                "configuracio.yml"
                )
        )
        return super().setUp()

    def tearDown(self):
        """ Es crida desprès de cada test """
        return super().tearDown()

    def test_create_configurador(self):
        self.configurador = self.create_configurador()
        
        assert self.configurador is not None, "NO s'ha creat un configurador [None]"
        assert type(self.configurador) is Configurador, "No s'ha creat un configurador [Wrong Type]"
        return 

    def test_get_persistencia_factory(self):
        pf = self.create_configurador().get_Persistencia_factory()
        assert issubclass(type(pf), Persistencia_factory)
        assert type(pf) is Persistencia_factory_mySql
        return

    def test_get_config(self):
        configuracio = self.create_configurador().get_config()
        assert configuracio is not None

    def create_configurador(self):
        return Configurador(
            os.path.join(
                os.path.dirname(__file__), 
                "configuracio.yml"
            )
        )
        
if __name__ == "__main__":
    unittest.main()