from api.config.initialization import ma
from api.modules.hotel.model import HotelModel, CurrencyModel


class HotelSchema(ma.ModelSchema):

    class Meta:
        model = HotelModel
        include_fk = True
        exclude = model.baseExcluded()


class CurrencySchema(ma.ModelSchema):

    class Meta:
        model = CurrencyModel
        include_fk = True
