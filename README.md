# AltaML-path-reader-api
A web API service that reads characters from a text file and generates a matrix path

## How To Start and Run the app
- Run `make run` in the terminal to start app on localhost:5000
- Visit this address `localhost:5000/api/v1/directions?filename=<filename>` to get the direction path
- `<filename>` is the name of the raw direction file placed in the directions folder without the `txt` extension
- You can also add your custom raw direction file to the directions folder. Valid direction operations are "F": to move forward, "L": to turn left and "R": to turn right.
- Check out the Makefile for other operations

## Available filenames
- directions-1
- directions-2
- directions-3
- directions-4
- directions-5
- directions-6
