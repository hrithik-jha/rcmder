# RCMDER
## Introduction
RCMDER is an entertainment recommendation API developed on Flask which accepts arguments via a Post request and returns a selection of movies or songs which is similar to the given item.

## Calling the API
The API has 2 routes. One for Movies and the other for Music.

### Movie
The POST request should send the name of a movie as an argument to get recommendations on the basis of it.
```
localhost:[PORT]/movie?title=[TITLE OF MOVIE]
```
A list of recommended movies is returned.

### Music
The POST request should send the name of the song and the album it belongs to as arguments to get recommendations.
```

```
A list of recommended songs is returned.
