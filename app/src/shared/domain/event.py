import uuid
import json
from datetime import datetime


class CloudEvent:
    """
    Representa un CloudEvent, que incluye atributos de contexto y datos del evento.
    """

    def __init__(
        self,
        type: str,
        source: str,
        data: dict,
        datacontenttype: str = "application/json",
    ):
        """
        Inicializa una instancia de CloudEvent.

        Args:
            type (str): El tipo de evento (por ejemplo, 'com.example.user.created').
            source (str): La fuente del evento (por ejemplo, 'https://my.app.com/users').
            data (dict): La carga útil o 'payload' del evento.
            datacontenttype (str): El tipo de medio de los datos, por defecto es 'application/json'.
        """
        self.id = str(uuid.uuid4())
        self.source = source
        self.specversion = "1.0"
        self.type = type
        self.datacontenttype = datacontenttype
        self.time = datetime.now().isoformat() + "Z"
        self.data = data

    def to_dict(self):
        """
        Convierte la instancia del CloudEvent en un diccionario para serialización.
        """
        return {
            "id": self.id,
            "source": self.source,
            "specversion": self.specversion,
            "type": self.type,
            "time": self.time,
            "datacontenttype": self.datacontenttype,
            "data": self.data,
        }

    def to_json(self):
        """
        Serializa la instancia del CloudEvent a una cadena JSON.
        """
        return json.dumps(self.to_dict())
