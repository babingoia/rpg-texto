#Fabricas para criação de views
#Libs
from interfaces import IViewFactory, IView
from .base import View

#Class
class ViewFactory(IViewFactory):
    @staticmethod
    def criar(tipo: str) -> IView:
        match tipo:
            case 'batalha':
                return View()
            case _:
                raise ValueError('Objeto não encontrado para instanciação!')