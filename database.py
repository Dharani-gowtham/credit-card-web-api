import time

import streamlit as st
# from streamlit_js_eval import get_geolocation


from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db_name = client["CreditCard"]


# loc = get_geolocation()

# latitude = loc["coords"]["latitude"]
# longitude = loc["coords"]["longitude"]


class CreditCard:
    def __init__(self, name, number, cvv, exp):
        self.name = name
        self.card_number = number
        self.cvv = cvv
        self.exp = exp
        self.brand = self.get_credit_card_brand()

    def get_credit_card_brand(self):
        card_number = str(self.card_number)
        if card_number.startswith('4'):
            return 'Visa'
        elif card_number.startswith(('51', '52', '53', '54', '55')):
            return 'Mastercard'
        elif card_number.startswith(('34', '37')):
            return 'American Express'
        elif card_number.startswith('6011') or (card_number.startswith(('622126', '622127', '622128', '622129', '62213',
                                                                        '62214', '62215', '62216', '62217', '62218',
                                                                        '62219', '6222', '6223', '6224', '6225', '6226',
                                                                        '6227', '6228', '6229', '623', '624', '625',
                                                                        '626', '627', '628', '629', '64',
                                                                        '65')) and len(card_number) == 16):
            return 'Discover'
        elif card_number.startswith(('300', '301', '302', '303', '304', '305', '36', '38')):
            return 'Diners Club'
        elif card_number.startswith(('35', '2131', '2132')):
            return 'JCB'
        elif card_number.startswith('62'):
            return 'UnionPay'
        else:
            return 'Unknown Brand'

def add_credit_card(name, number, cvv, exp):
    card = vars(CreditCard(name=name, number=number, cvv=cvv, exp=exp))
    db_collection = db_name["Cards"]
    db_collection.insert_one(card)


def get_credit_cards():
    db_collection = db_name["Cards"]
    cards = list(db_collection.find())
    return cards

def delete_credit_card(id):
    db_collection = db_name["Cards"]
    db_collection.delete_one({'_id': ObjectId(id)})

