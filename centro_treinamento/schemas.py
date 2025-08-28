from typing import Annotated

from pydantic import Field
from contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", examples='Centro A', max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do centro de treinamento", examples='Rua 1, 123', max_length=60)]
    proprietario: Annotated[str, Field(description="Nome do proprietário do centro de treinamento", examples='João Silva', max_length=30)]
