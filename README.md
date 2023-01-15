# StudyCam

Created by Sabrina Punjani, Kai Wang, Marwan Ali, and Sydney Sochaj at **DeltaHacks 9**

## Inspiration

We created this project with the intention of helping people stay focused when studying, while monitoring their health over a study session.

## What it does

StudyCam uses your webcam to track how long you've been studying, and uses computer vision to keep track of a variety of information relating to distractions, including how many times you left your study area, and the duration of time that you were gone for.

## How we built it

Python, OpenCV, PyQt6

1. The user starts the program by clicking "start" on the GUI
2. StudyCam starts to keep track of the user's face using OpenCV face detection technologies
3. If the user leaves their study area for too long, StudyCam will start keeping track of information such as time gone, and amount of absences.
4. Once the user finishes their study session, they will be presented with a detailed summary of their session.

## Challenges we ran into

We had a great deal of difficulty working with OpenCV and optimizing their prebuilt models for our specific use case. Specifically, oftentimes in our project, the webcam wasn't directly viewing the front of a person's face, as people usually study with their heads facing down. We had to fine tune the model to be able to detect the noisy data, in addition to being able to track when the person left the frame.

## Accomplishments we're proud of

None of us had ever extensively used OpenCV before, or frankly any form of computer vision, so we're proud that we were able to implement such an advanced topic into our project.

## What we learned

- How computer vision works, and how to fine tune prebuilt models for personal usage
- How to communicate data in between a front end GUI, an external REST API, and a backend program

## What's next?

We have a lot of ideas for future additions that we didn't have time to implement this weekend at DeltaHacks:

1. Implement functionality into a chrome extension
2. More detailed reports, maybe include information such as total break time
3. More accurate face/studying detection
4. Analyze data from multiple study sessions to give user insightful data on their study habits
