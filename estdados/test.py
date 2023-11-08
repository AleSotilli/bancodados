import unittest

from main import Paciente, criar_fila_prioridades, inserir_paciente, remover_paciente


class TestPaciente(unittest.TestCase):

    def test_init(self):
        paciente = Paciente("João", 25, 1)
        self.assertEqual(paciente.nome, "João")
        self.assertEqual(paciente.idade, 25)
        self.assertEqual(paciente.prioridade, 1)

    def test_lt(self):
        paciente1 = Paciente("João", 25, 1)
        paciente2 = Paciente("Maria", 50, 2)
        self.assertTrue(paciente1 < paciente2)


class TestCriarFilaPrioridades(unittest.TestCase):

    def test_criar_fila_vazia(self):
        fila = criar_fila_prioridades()
        self.assertEqual(len(fila), 0)


class TestInserirPaciente(unittest.TestCase):

    def test_inserir_paciente(self):
        fila = criar_fila_prioridades()
        paciente = Paciente("João", 25, 1)
        inserir_paciente(fila, paciente)
        self.assertEqual(len(fila), 1)


class TestRemoverPaciente(unittest.TestCase):

    def test_remover_paciente(self):
        fila = criar_fila_prioridades()
        paciente = Paciente("João", 25, 1)
        inserir_paciente(fila, paciente)
        paciente_removido = remover_paciente(fila)
        self.assertEqual(paciente_removido.nome, "João")
        self.assertEqual(len(fila), 0)


if __name__ == "__main__":
    unittest.main()
