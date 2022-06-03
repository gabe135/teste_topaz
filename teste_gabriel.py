import requests
import unittest

def get_username(username: str) -> dict:
    url = f"https://api.github.com/users/{username}"
    user_data = requests.get(url).json()
    return user_data

# usuario = input('Entre com um usuário Git: ')
userdados = get_username('gabe135')


class User:

    def __init__(self, user):
        userdata = get_username(user)
        self.login = userdata['login']
        self.id = userdata['id']
        self.avatar_url = userdata['avatar_url']
        self.html_url = userdata['html_url']

    def imprime(self):
        print('login: ' + str(self.login) + '\nid: ' + str(self.id) + '\navatar url: ' +
                   str(self.avatar_url) + '\nhtml url: ' + str(self.html_url))

    def atributos(self):
        # lista de atributos p/ teste
        return [self.login, self.id, self.avatar_url, self.html_url]

class TestMethods(unittest.TestCase):

    """Classe de testes unitários. Crie seus testes aqui."""

    def test_this_test_words(self):

        self.assertTrue(True)

    def test_username_parameters(self):

        parameters = ['login', 'id', 'avatar_url', 'html_url']

        response = get_username('gabe135')

        for param in parameters:

            self.assertTrue(param in response.keys())

    def test_get_username(self):

        expected = ['gabe135', 106398557]

        parameters = ['login', 'id']
        response = get_username('gabe135')
        x = [ response[param] for param in parameters ]

        for i in range(0, len(x)):
            self.assertEqual(expected[i], x[i])

    def test_User(self):

        parameters = ['login', 'id', 'avatar_url', 'html_url']
        response = get_username('gabe135')
        x = [response[x] for x in parameters]

        gabriel = User('gabe135')

        for i in range(0, len(x)):
            self.assertEqual(x[i], gabriel.atributos()[i])


if __name__ == "__main__":

    unittest.main()