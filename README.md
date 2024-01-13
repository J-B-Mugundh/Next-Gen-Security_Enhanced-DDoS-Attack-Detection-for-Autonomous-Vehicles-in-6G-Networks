# Advanced DDoS Attack Detection in Autonomous Vehicles

## Table of Contents

- [Introduction](#introduction)
- [Authors](#authors)
- [Abstract](#abstract)
- [Repo Structure](#repository-structure)
- [Usage](#usage)
- [Proposed Work](#proposed-work)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The "Advanced DDoS Attack Detection in Autonomous Vehicles" research project focuses on enhancing the cybersecurity of autonomous vehicles, particularly by detecting Distributed Denial of Service (DDoS) attacks and other cyber threats. This README provides an overview of the project's objectives, methods, and results.

## Authors

- **Mugundh J B** (2021503524)
- **Vijai Suria M** (2021503558)

## Abstract

Autonomous vehicles have gained prominence in smart cities, and their reliance on wireless communication makes them susceptible to cyberattacks, including DDoS attacks, GPS spoofing, and malware injection. This research project introduces an intrusion detection system (IDS) powered by machine learning to safeguard autonomous vehicle networks. It involves:

- Data preprocessing to prepare the dataset.
- Application of machine learning algorithms for DDoS attack detection.
- Evaluation of the effectiveness of different algorithms.
- Proposed algorithms for autonomous vehicle modules and software.

## Repository Structure

### 1. Simulation folder

- Contains records to simulate DDoS attacks in the SUMO (Simulation of Urban MObility) simulator.

### 2. ADADS_using_HDM_and_CLM.ipynb

- Jupyter notebook containing the code for implementing Anomaly Detection for DDoS Attacks using a Hybrid Detection Model (HDM) and Continuous Learning Model (CLM).
- Provides graphical visualization of results and records for interpreting the outcomes.

### 3. Hybrid_Models_Individual.ipynb

- Jupyter notebook containing the code for individual machine learning models.
- Includes code for five classifiers: Naive Bayes (NB), Random Forest (RF), Logistic Regression (LR), Support Vector Machines (SVM), and K-Nearest Neighbors (KNN).

## Usage

1.  Navigate to the `Simulation` folder to access records for simulating DDoS attacks in the SUMO simulator.
2.  Open the `ADADS_using_HDM_and_CLM.ipynb` notebook to view and run the code for implementing the Anomaly Detection system using a Hybrid Detection Model and Continuous Learning Model.
3.  Explore the `Hybrid_Models_Individual.ipynb` notebook to understand the implementation of individual machine learning models.

## Proposed Work

The proposed work includes the development of an intrusion detection system that aims to detect DDoS attacks. It utilizes advanced machine learning algorithms, such as _Naive Bayes, Random Forest, Logistic Regression, K-Nearest Neighbors (KNN), and Support Vector Machines (SVM)_.
The DDoS attack detection algorithm improves the security of autonomous vehicles by identifying DDoS attacks using Wi-Fi Intrusion Detection System. It involves data preprocessing, feature selection, and the application of machine learning classifiers to detect and analyze DDoS attacks.
To improve accuracy and stability, a hybrid model combines results from five ML models using a **soft voting mechanism**. Each model's weight is determined through a mathematical probability model, resulting in a robust defense against DDoS attacks.
Also, our **continuous learning model** is designed to continually update and enhance a Classifier for the purpose of efficiently handling incoming data streams, particularly in the context of DDoS attack detection. The model is initialized using various libraries, and it starts by loading an initial dataset. It then enters a continuous update loop, where new data is continuously loaded and appended to the existing dataset, ensuring that the model adapts to changing conditions.

## Contributing

We welcome contributions from other students and developers to improve and enhance this project. If you'd like to contribute, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and commit them with a descriptive commit message.

4. Push your changes to your fork.

5. Create a pull request to the original repository, explaining your changes and why they should be merged.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to contact us:

- Vijai Suria M: [LinkedIn](https://linkedin.com/in/vijaisuria)
- Mugundh J B: [LinkedIn](https://linkedin.com/in/mugundhjb)
