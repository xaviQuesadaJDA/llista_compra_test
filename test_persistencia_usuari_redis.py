#!/usr/bin/python3


"""
    Test de la Classe Persistencia_factory_mySql de la llista de la compra
"""
import unittest
import bcrypt
import sys, os, shutil
sys.path.append("../Public_llista_compra_m06/")
from Configurador import Configurador
from Usuari import Usuari

class test_Persistencia_factory_redis(unittest.TestCase):
    USUARI_TEST = "usuari de test"
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
        self.pu = self.pf.get_Persistencia_usuari_factory()
        return super().setUp()

    def tearDown(self):
        """ Es crida desprès de cada test """
        self.configurador = None
        self.pf = None
        self.pu = None
        return super().tearDown()

    def test_desa_get_delete(self):
        usuari = self.crea_usuari()
        nova_id = self.pu.desa(usuari)
        assert type(nova_id) is str
        assert type(self.pu.get(nova_id)) is Usuari
        rewrite_id = self.pu.desa(usuari)
        assert rewrite_id == nova_id # Only 1 user should be created
        deleted = self.pu.delete(nova_id)
        assert deleted
        usuari = self.crea_usuari()
        nova_id = self.pu.desa(usuari)
        usuari.set_id(nova_id)
        assert type(nova_id) is str
        api_key = "no_existeix"
        assert self.pu.get_from_apikey(api_key) is None
        api_key = "si_existeix"
        self.pu.set_sessio(api_key, usuari)
        assert self.pu.get_from_apikey(api_key).get_nom() == usuari.get_nom()
        deleted = self.pu.delete(nova_id)
        assert deleted
        return
    
    def test_llista(self):
        llista = self.pu.get_llista()
        assert llista is not None
        id_a_esborrar = False
        for usuari in llista:
            if usuari.get_nom() == self.USUARI_TEST:
                id_a_esborrar = usuari.get_id()
        if id_a_esborrar:
            self.pu.delete(id_a_esborrar)

    def crea_usuari(self):
        return Usuari(
            self.pu, 
            None, 
            self.USUARI_TEST,
            bcrypt.hashpw("1234".encode(), bcrypt.gensalt())
            )

        
if __name__ == "__main__":
    unittest.main()