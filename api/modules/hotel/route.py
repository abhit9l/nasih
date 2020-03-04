from api.modules.hotel.resource import ns_hotel, Hotel, StaticData, IATACode, HotelOffer

ns_hotel.add_resource(Hotel, '/')
ns_hotel.add_resource(StaticData, '/staticdata')
ns_hotel.add_resource(IATACode, '/<string:keyword>')
ns_hotel.add_resource(HotelOffer, '/offer/')
