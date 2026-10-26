from flask_restful import Resource, reqparse
from models.hotel import HotelModel

class Hoteis(Resource):
    def get(self):
        return ({"hoteis": [hotel.json() for hotel in HotelModel.query.all()]})

# Listar, inserir, atualizar e eliminar um hotel especifico

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("Nome", type = str, help="Nome obrigatório")
    argumentos.add_argument("estrelas", type = float, help="Estrelas obrigatório")
    argumentos.add_argument("diaria", type = float, help="Diaria obrigatório")
    argumentos.add_argument("cidade", type = str, help="Cidade obrigatório")
    def get(self, id_hotel):
        hotel_encontrado =HotelModel.find_hotel(id_hotel)
        if hotel_encontrado:
                return hotel_encontrado.json(), 200
        return {"mensage": "Hotel not found"}, 404

    def post(self,id_hotel):
        dados = Hotel.argumentos.parse_args() #Dicionário
        for hotel in hoteis:
             if hotel["hotel_id"] == id_hotel:
                return {"message": "Hotel with this id already exists"}
        
        novo_hotel = HotelModel (id_hotel, **dados )
        novo_hotel .save_hotel()
        return novo_hotel.json(), 200

    def put(self,id_hotel):
            dados = Hotel.argumentos.parse_args() #Dicionário
            hotel_encontrado = HotelModel.find_hotel(id_hotel)
            if hotel_encontrado :
                    hotel_atualido = HotelModel ( id_hotel, **dados)
                    hotel.atualizado,update_hotel (**dados)
                    hotel_atualido.savehotel()
                    return hotel_atualido.json(), 200
                 
            novo_hotel = {"hote_id": id_hotel, **dados }
            hoteis.append(novo_hotel)
            return novo_hotel, 201 #Created

    def delete (self, id_hotel):
        global hoteis 
        hoteis = [hotel for hotel in hoteis if hotel["hotel_id"] != id_hotel]
        return { "message": f"Hotel with {id_hotel} deleted "}
