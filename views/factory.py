#Fabricas para criação de views
#Libs
from interfaces import IViewFactory, IView
from .batalha_view import BatalhaView

#Class
class ViewFactory(IViewFactory):
    @staticmethod
    def criar(tipo: str) -> IView:
        match tipo:
            case 'batalha':
                return BatalhaView()
            case _:
                raise ValueError('Objeto não encontrado para instanciação!')