import pytest

def execute_tests():
    print("Ejecutando test cases de recepcionista...")
    pytest.main(["-s", "-v", "./test_cases/test_nombre_modulo/"])

    print("Pruebas Finalizadas")

if __name__ == "__main__":
    execute_tests()
