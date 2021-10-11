import requests
import random
import json
async def get_wallpaper(genre):
    if not genre:
        #Pick random genre from call back
        response = requests.get("https://cuy-api.herokuapp.com/api/wallpapers/")
        responseJSON = json.loads(response.content)
        genreArray = responseJSON['Genres']
        randomint = random.randint(0, (len(genreArray) - 1))
        genreRandom = genreArray[randomint]


        #Pick random image from call back
        imageResponse = requests.get("https://cuy-api.herokuapp.com/api/wallpapers/{}".format(genreRandom))
        imageResponseJSON = json.loads(imageResponse.content)
        imageArray = imageResponseJSON['list']
        randomImageInt = random.randint(0, (len(imageArray) - 1))
        imageRandom = imageArray[randomImageInt]

        #Return the final URL
        return "https://cuy-api.herokuapp.com/api/wallpapers/{}/{}".format(genreRandom, imageRandom)

    response = requests.get("https://cuy-api.herokuapp.com/api/wallpapers/{}".format(genre))
    if genre.lower() == "list":
        response = requests.get("https://cuy-api.herokuapp.com/api/wallpapers/")
        responseJSON = json.loads(response.content)
        genreArray = responseJSON['Genres']
        finalArray = []
        for genre in genreArray:
            parsedGenre = "`" + genre + "`" + ","
            finalArray.append(parsedGenre)
        return "Here is a list of the available genres: \n" + "".join(finalArray)

    
    responseJSON = json.loads(response.content)
    if responseJSON['Status'] == 404: return "Genre not found!"
    imageArray = responseJSON['list']
    randomInt = random.randint(0, (len(imageArray)-1))
    imageFile = imageArray[randomInt]
    return "https://cuy-api.herokuapp.com/api/wallpapers/{}/{}".format(genre, imageFile)
        


