#!/usr/bin/python3


"""
    Test de la Classe Persistencia_factory_redis de la llista de la compra
"""
import unittest
import sys, os, shutil
sys.path.append("../Public_llista_compra_m06/")
from Configurador import Configurador
from Persistencia_factory import Persistencia_factory
from Persistencia_usuari import Persistencia_usuari
from Persistencia_usuari_redis import Persistencia_usuari_redis


class test_Persistencia_factory_redis(unittest.TestCase):

    def setUp(self):
        """ Es crida abans de cada test """
        # Set configuracio_mysql.yml as config file
        shutil.copyfile(
            os.path.join(
                os.path.dirname(__file__), 
                "configuracio_redis.yml"
                ),
            os.path.join(
                os.path.dirname(__file__), 
                "configuracio.yml"
                )
        )
        self.configurador = Configurador(
                os.path.join(
                os.path.dirname(__file__), 
                "configuracio.yml"
            )
        )
        self.pf = self.configurador.get_Persistencia_factory()
        return super().setUp()

    def tearDown(self):
        """ Es crida desprès de cada test """
        self.configurador = None
        self.pf = None
        return super().tearDown()

    def test_get_Persistencia_usuari_factory(self):
        p_usuari = self.pf.get_Persistencia_usuari_factory()
        assert issubclass(type(p_usuari), Persistencia_usuari)
        assert type(p_usuari) is Persistencia_usuari_redis
        return

        
if __name__ == "__main__":
    unittest.main()