# EWBeyond-AI-Security-System-Demo
This was a prototype of what an AI security system that could be implemented in pubic transportation would look like. This was made as a part of my group's case study project for the Engineers Without Borderer Case Study Showcase (2024) at the University of Toronto St. George campus.

This “prototype” is trained to detect only dangerous weapons, a banana was used as a placeholder for a weapon/dangerous object as it is a simple object in appearance to train an AI model on. The very simple detection model was made using the Python Opencv library. 

The code implements machine learning with the built in opencv cascade classifier for detection, which is usually used for facial detection, but has been used to detect a banana. The cascade classifier utilizes Haar cascade object detection, which is a method proposed by Paul Viola and Michael Jones in their paper, "Rapid Object Detection using a Boosted Cascade of Simple Features" in 2001.


#How to Run Code

Open the files in any python IDE and run the banana.py file.
