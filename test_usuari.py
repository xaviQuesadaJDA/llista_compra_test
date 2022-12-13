#!/usr/bin/python3


"""
    Test de la Classe Persistencia_factory_mySql de la llista de la compra
"""
import uuid
import unittest
import bcrypt
import sys, os, shutil
sys.path.append("../Public_llista_compra_m06/")
from Configurador import Configurador
from Usuari import Usuari

class SimpleTestCase(unittest.TestCase):
    USUARI_TEST = "usuari de test"
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
        self.configurador = Configurador(
                os.path.join(
                os.path.dirname(__file__), 
                "configuracio.yml"
            )
        )
        self.pf = self.configurador.get_Persistencia_factory()
        self.pu = self.pf.get_Persistencia_usuari_factory()
        return super().setUp()

    def tearDown(self):
        """ Es crida desprès de cada test """
        self.configurador = None
        self.pf = None
        self.pu = None
        return super().tearDown()

    def test_usuari(self):
        usuari = self.crea_usuari()
        assert type(usuari.desa()) is Usuari
        assert usuari.get_nom() == self.USUARI_TEST
        assert type(usuari.get_id()) is int
        assert usuari.get_password_hash() is not None
        # x_api_key = usuari.set_sessio(str(uuid.uuid4()))
        # assert type(x_api_key) is str
        assert usuari.delete()
        return
    
    def crea_usuari(self):
        return Usuari(
            self.pu, 
            None, 
            self.USUARI_TEST,
            bcrypt.hashpw("1234".encode(), bcrypt.gensalt())
            )

        
if __name__ == "__main__":
    unittest.main()