from algorithms.alberti.alberti import *
from algorithms.alberti.config import *

class AlbertiCircleMode1():
    @staticmethod
    def check_validity(data: dict) -> bool:
        return all([i.upper() in ALPHABET for i in data['ciphertext']]) and \
                all([i.upper() in ALPHABET for i in data['key']]) and \
                len(data["key"]) == len(ALPHABET)
    
    @staticmethod
    def fix_data_fields(data: dict):
        data["ciphertext"] = data["ciphertext"].upper()
        data["key"] = data["key"].upper()

    @staticmethod
    def encrypt(data: dict):
        if not AlbertiCircleMode1.check_validity(data): return {"status": 400, "error": "Not valid data"}
        AlbertiCircleMode1.fix_data_fields(data)
        return {
            "ciphertext": data['ciphertext'],
            "key": data["key"],
            "password": "",
            "indicator": "",
            "plaintext": encrypt_mode1(data['ciphertext'], data["key"])
        }

    @staticmethod
    def decrypt(data: dict):
        if not AlbertiCircleMode1.check_validity(data): return {"status": 400, "error": "Not valid data"}
        AlbertiCircleMode1.fix_data_fields(data)
        return {
            "ciphertext": data['ciphertext'],
            "key": data["key"],
            "password": "",
            "indicator": "",
            "plaintext": decrypt_mode1(data['ciphertext'], data["key"])
        }

class AlbertiCircleMode2():
    @staticmethod
    def check_validity(data: dict) -> bool:
        return all([i.upper() in ALPHABET for i in data['ciphertext']]) and \
                all([i.upper() in ALPHABET for i in data['key']]) and \
                len(data["key"]) == len(ALPHABET)
    
    @staticmethod
    def fix_data_fields(data: dict):
        data["ciphertext"] = data["ciphertext"].upper()
        data["key"] = data["key"].upper()

    @staticmethod
    def encrypt(data: dict):
        if not AlbertiCircleMode2.check_validity(data): return {"status": 400, "error": "Not valid data"}
        AlbertiCircleMode2.fix_data_fields(data)
        return {
            "ciphertext": data['ciphertext'],
            "key": data["key"],
            "password": "",
            "indicator": "",
            "plaintext": encrypt_mode2(data['ciphertext'], data["key"])
        }

    @staticmethod
    def decrypt(data: dict):
        if not AlbertiCircleMode2.check_validity(data): return {"status": 400, "error": "Not valid data"}
        AlbertiCircleMode2.fix_data_fields(data)
        return {
            "ciphertext": data['ciphertext'],
            "key": data["key"],
            "password": "",
            "indicator": "",
            "plaintext": decrypt_mode2(data['ciphertext'], data["key"])
        }

class AlbertiCircleMode3():
    @staticmethod
    def check_validity(data: dict) -> bool:
        return all([i.upper() in ALPHABET for i in data['ciphertext']]) and \
                all([i.upper() in ALPHABET for i in data['key']]) and \
                len(data["indicator"]) < 2 and all([i.upper() in ALPHABET for i in data['indicator']]) and \
                len(data["key"]) == len(ALPHABET)
    
    @staticmethod
    def fix_data_fields(data: dict):
        data["ciphertext"] = data["ciphertext"].upper()
        data["key"] = data["key"].upper()
        data["indicator"] = data["indicator"].upper()

    @staticmethod
    def encrypt(data: dict):
        if not AlbertiCircleMode3.check_validity(data): return {"status": 400, "error": "Not valid data"}
        AlbertiCircleMode3.fix_data_fields(data)
        return {
            "ciphertext": data['ciphertext'],
            "key": data["key"],
            "password": "",
            "indicator": data["indicator"],
            "plaintext": encrypt_mode3(data['ciphertext'], data["key"], data["indicator"])
        }

    @staticmethod
    def decrypt(data: dict):
        if not AlbertiCircleMode3.check_validity(data): return {"status": 400, "error": "Not valid data"}
        AlbertiCircleMode3.fix_data_fields(data)
        return {
            "ciphertext": data['ciphertext'],
            "key": data["key"],
            "password": "",
            "indicator": data["indicator"],
            "plaintext": decrypt_mode3(data['ciphertext'], data["key"], data["indicator"])
        }

class AlbertiCircleMode4():
    @staticmethod
    def check_validity(data: dict) -> bool:
        return all([i.upper() in ALPHABET for i in data['ciphertext']]) and \
                all([i.upper() in ALPHABET for i in data['key']]) and \
                len(data["key"]) == len(ALPHABET)
    
    @staticmethod
    def fix_data_fields(data: dict):
        data["key"] = data["key"].upper()

    @staticmethod
    def encrypt(data: dict):
        if not AlbertiCircleMode4.check_validity(data): return {"status": 400, "error": "Not valid data"}
        AlbertiCircleMode4.fix_data_fields(data)
        return {
            "ciphertext": data['ciphertext'],
            "key": data["key"],
            "password": "",
            "indicator": "",
            "plaintext": encrypt_mode4(data['ciphertext'], data["key"])
        }

    @staticmethod
    def decrypt(data: dict):
        if not AlbertiCircleMode4.check_validity(data): return {"status": 400, "error": "Not valid data"}
        AlbertiCircleMode4.fix_data_fields(data)
        return {
            "ciphertext": data['ciphertext'],
            "key": data["key"],
            "password": "",
            "indicator": "",
            "plaintext": decrypt_mode4(data['ciphertext'], data["key"])
        }

class AlbertiCircleMode5():
    @staticmethod
    def check_validity(data: dict) -> bool:
        return all([i.upper() in ALPHABET for i in data['ciphertext']]) and \
                all([i.upper() in ALPHABET for i in data['key']]) and \
                all([i.upper() in ALPHABET for i in data['password']]) and \
                len(data["key"]) == len(ALPHABET)
    
    @staticmethod
    def fix_data_fields(data: dict):
        data["ciphertext"] = data["ciphertext"].upper()
        data["key"] = data["key"].upper()
        data["password"] = data["password"].upper()

    @staticmethod
    def encrypt(data: dict):
        if not AlbertiCircleMode5.check_validity(data): return {"status": 400, "error": "Not valid data"}
        AlbertiCircleMode5.fix_data_fields(data)
        return {
            "ciphertext": data['ciphertext'],
            "key": data["key"],
            "password": data["password"],
            "indicator": "",
            "plaintext": encrypt_mode5(data['ciphertext'], data["key"], data["password"])
        }

    @staticmethod
    def decrypt(data: dict):
        if not AlbertiCircleMode5.check_validity(data): return {"status": 400, "error": "Not valid data"}
        AlbertiCircleMode5.fix_data_fields(data)
        return {
            "ciphertext": data['ciphertext'],
            "key": data["key"],
            "password": data["password"],
            "indicator": "",
            "plaintext": decrypt_mode5(data['ciphertext'], data["key"], data["password"])
        }


