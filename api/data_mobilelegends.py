import requests
import json

def send_code(gameId):
    response = requests.get("https://api.mobilelegends.com/mlweb/sendMail?roleId={}&language=en".format(gameId))
    data_json = json.loads(response.text)

    if data_json["status"] == "error":
        return ("Game Id {} tidak ada\n\nSilahkan masukan Game Id yang benar".format(gameId))
    else:
        return("Verifikasi code sudah kekirim, silakan cek diemail mobile legends anda")

def send_redeem(gameId, verifikasi, redeem):
    post_data = {
        "redeemCode": redeem,
        "roleId": gameId,
        "vCode": verifikasi,
        "language": "en"
    }

    response = requests.post("https://api.mobilelegends.com/mlweb/sendCdk", data=post_data)
    data_json = json.loads(response.text)

    if data_json["status"] == "error":
        return("Kode verifikasi tidak benar atau kode redeem tidak ditemukan")
    else:
        return(":clap: yeay berhasil kode redeem telah dikirim")

