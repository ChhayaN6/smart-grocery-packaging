# Smart Grocery Packaging Using KNN Algorithm

## Problem Statement
Food spoilage leads to health risks and economic loss. This project proposes a Smart Grocery Packaging system that determines food freshness using sensor data and machine learning.

## Objective
To classify food as Fresh or Spoiled using the K-Nearest Neighbors (KNN) algorithm based on environmental conditions.

## Sensors Used
- Temperature Sensor
- Humidity Sensor
- Gas Sensor (MQ series)

## Features Used
- Temperature
- Humidity
- Gas level

## Machine Learning Algorithm
### K-Nearest Neighbors (KNN)
KNN is a supervised machine learning algorithm that classifies data based on the majority class of its nearest neighbors.

### Variations of KNN Used
- Distance-based KNN (Euclidean distance)
- Weighted KNN
- Different values of K for optimization
- Feature scaling for accurate distance calculation

## System Workflow
1. Sensors collect real-time data
2. Data is sent to the Firebase database
3. KNN model predicts Fresh or Spoiled
4. Result is displayed on LCD / App

## Result
The system accurately classifies food freshness using KNN and provides real-time monitoring.

## Tools & Technologies
- Python
- Firebase Database
- KNN Algorithm
- Machine Learning
- Sensors
- GitHub

## Report
The complete project report is available in the `report` folder.
