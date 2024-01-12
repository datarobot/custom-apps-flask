To run this in DR Custom apps:
1. Build the custom app `docker build . -t my-flask-app`
2. Save the custom app `docker save my-flask-app -o myFlaskApp.tgz`
3. Navigate to DataRobot's Applications page and upload the app there.

Troubleshooting:
* Some computers (eg M1 Macbooks) require docker images to be built via `docker buildx build --platform linux/amd64 . -t custom-apps-flask`. This requires Docker Desktop, which requires a seperate license.
