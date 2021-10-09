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
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDOQcH2f9Fx2DZa\n/6bKuVxHhUD6YjkkHNoubUKcqn2V/mPukrKGgOeNLgVTnVpdeZpGcj0mk2TmyriQ\n/INjagzEoWsL25RPwdn6xgCnhjrA4T4scNuqVL/K97XptGe4fE9vElixhFOzgAbJ\nkdqjOTdhsvPEOsceueCiqdSBzh+15MZwNrPSrZbiLFNr0oh71HTOjieEdGr4k3PL\nKoaSTKs1rMomwtijImVcwInGYHotX2kKRh/GZD12PpVy9xYg0E3Cb5Xl1U+0M185\n3ZTRyG7p8owk61+xUYZIR3aMYqZVJktRbA37u804Yp0TscSs25wquINjyH05eJN2\nolyTM0JhAgMBAAECggEACj+xPCboyN/l/4qRhqRERheEfYyQ6071tnXeZ/t+xwu/\nenTWoyFXoCfHwvpgKaHnvRVjHX4YdvFez3GEs9VqsgCVWZ79FSN8Sd453Rkp5Tis\nBrhK6gFREGxToTvCJaQjrFC8kIGTSSmU7MIvG4o1ysiCHV+QUmIJG/wVX6fW4opX\nRHzRYWI17YAHEQAaHiB4fUPQXXKwB/rYgRwsUsDNDRObnIaRLDFBbxhSLjrFyxcV\neFryfYPgcj7D4yG2ik6NFpljlY7c/jW7uwRCoKuyRTIgzlqD6gcpvJdDL5DltWvr\n5OKSixnTJbA/zpHCoDCl/AGFl0Jr91U039wKL/65GQKBgQDzKXWv+TDdEQKMtTYl\nX2VoB3yfUkaPZ32jNEMNbRRwKayhQaiVfeZ7xOaWuS7fh1wT0z/TL/pJ7uJz6cdY\nRfmD6n0EIUzCedURLMmzjScUW+Qy+ggTTu6LZXp00Z1gZzhI++rrc/B7i+X6QzXX\nhrALGvZ4WL0k7qActlNcSc6DdQKBgQDZJX6PGEqB8ldJj5EY2BLeQpVaqLjOWMT2\nrjLeDLjlBAJOiiJsHweB9Hm+95RCpzOsrPL5BqSZT9fbG43dsO5/ixsoeJkskZwj\nTkl7ZHFTkSFBHRsDY8GbqrYR0bgBZNwFfmKjmQVGoLQEvWpXW5rUBt/UWKw05Z54\nofiaUv3BvQKBgQCIsPDIeJOgYhSF1sRWY/cUcMj8ovqpWKsG2LUs0fngR30UtV04\nlCrBvuFFL1qLK4N2XZWOeXUApLpGIM//7m4iWunmLXYCCQzed8f3GE00o6d3hJiP\nihqM4AHjs4X9kGjSllLsAyPXv8ALXEbjHoLN611ML847+aymF1RrF85wlQKBgA9u\n/MnK3jDSOqX90EBFy0GE1fy1lT0FTiqCQxdJLDMKz+cpJj0tD2mLKMQL8Lu0CpYx\nTKuqbzR+Wkc2dCTXmHv0NR/xQmHKj6BqxgpBH1TjMcvg97SL+IzJ21r03vEqbADv\n9K7QB3H3phPYKqC+4AhF3M7I5qRz1YmZaYP+dg65AoGAOa198XEeW6RWIPx7Ok0L\nhkHMSfCaJFR8+FoxeMe2BGPd6RaJWtec2PaoWnKWC83vYOUy0JVGKlWYkX6ZPIfw\ncIoqBl3tfZvTxoYOKn5qt+Q0dylt/PIyaxrIntIpzR/tSohFMBnxDR7DYO85sK12\nlarn8kbhvWKCva6HYvrYqdg=\n-----END PRIVATE KEY-----\n",
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
