import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # testes para tipos inválidos e verifica se retornar uma exceção
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(3, 3)
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("test", "error")

    # teste para casos de uma key ímpar
    initial_message = "123456"
    assert_message = "321_654"
    assert encrypt_message(initial_message, 3) == assert_message

    # teste para casos de uma key par
    initial_message = "123456"
    assert_message = "6543_21"
    assert encrypt_message(initial_message, 2) == assert_message

    # teste para casos de uma key válida porém sem índice na messagem
    initial_message = "87263"
    assert_message = "36278"
    assert encrypt_message(initial_message, 8) == assert_message
