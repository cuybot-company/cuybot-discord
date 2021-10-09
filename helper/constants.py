import discord, os
from datetime import datetime

request_help = ["cuy/help", "cuy/bantuan", "cuy/command"]
request_stat = ["cuy/status", "cuy/stat", "cuy/stats", "cuy/test", "cuy/ping"]
request_welcome = ["cuy/hi", "cuy/helo", "cuy/hello", "cuy/halo", "cuy/hai"]
request_quote = ["cuy/quotes", "cuy/quote", "cuy/kutipan"]
request_lyric = ["cuy/lirik", "cuy/lyric", "cuy/lyrics"]
request_mobile = ["cuy/mobile", "cuy/hp", "cuy/handphone", "cuy/phone"]
request_new_mobile = ["baru", "terbaru", "new"]
request_g_credentials = {
    "type": os.getenv("G_TYPE"),
    "project_id": os.getenv("G_PROJECT_ID"),
    "private_key_id": os.getenv("G_PRIVATE_KEY_ID"),
    "private_key": "-----BEGIN PUBLIC KEY-----\n" + os.getenv("G_PRIVATE_KEY") + "\n-----END PUBLIC KEY-----",
    "client_email": os.getenv("G_CLIENT_EMAIL"),
    "client_id": os.getenv("G_CLIENT_ID"),
    "auth_uri": os.getenv("G_AUTH_URI"),
    "token_uri": os.getenv("G_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("G_AUTH_PROVIDER"),
    "client_x509_cert_url": os.getenv("G_CLIENT_CERT")
}
data_covid_from = 'https://data.covid19.go.id'
today = datetime.today().strftime('%YY-%MM-%DD')
client = discord.Client()
