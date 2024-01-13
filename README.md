# Next-Gen-Security-Enhanced-DDoS-Attack-Detection-for-Autonomous-Vehicles-in-6G-Networks

## Authors

- **Mugundh Jambukeswaran Bhooma, Department of Computer Technology, MIT Campus, Anna University, Chennai.**
- **Vijai Suria Marimuthu, Department of Computer Technology, MIT Campus, Anna University, Chennai.**

## Abstract

Autonomous Vehicles (AVs) powered by 6G technologies have transformed transportation, but their reliance on the Internet of Vehicles (IoV) makes them vulnerable to cyber threats. Distributed Denial of Service (DDoS) attacks pose a significant risk, impacting AV safety. This paper introduces the Advanced DDoS Attack Detection System (ADADS) using a Hybrid Detection Model (HDM) and Continuous Learning Model (CLM) for dynamic adaptation to evolving attack patterns.

## Keywords

- Autonomous Vehicles
- 6G Communications
- DDoS Attack Detection
- Hybrid Detection Model
- Continuous Learning Model

## Introduction

![Attack Scenario](https://github.com/J-B-Mugundh/Next-Gen-Security-Enhanced-DDoS-Attack-Detection-for-Autonomous-Vehicles-in-6G-Networks/blob/main/attack-scenario-6g.png)

The advent of AVs brings enhanced safety and reduced environmental impact, relying on advanced technologies like smart driving instruments and Machine Learning (ML). However, the increasing connectivity exposes them to cyber threats, with DDoS attacks being a prominent concern. Existing DDoS detection systems face challenges in adapting to evolving attack patterns.

## Related Works

Several works have focused on DDoS detection using ensemble techniques and ML/DL approaches. However, most frameworks lack adaptability to newly evolving attack patterns. The proposed ADADS leverages a comprehensive HDM and CLM to enhance accuracy and adaptability in 6G networks.

## Advanced DDoS Attack Detection System (ADADS)

![Architecture Diagram](https://github.com/J-B-Mugundh/Next-Gen-Security-Enhanced-DDoS-Attack-Detection-for-Autonomous-Vehicles-in-6G-Networks/blob/main/adads_arch_diagram.png)

ADADS employs a Hybrid Detection Model (HDM) featuring ML algorithms (NB, RF, LR, KNN, SVM) trained on the "CIC-DDoS2019" dataset for effective DDoS attack detection. The Continuous Learning Model (CLM) ensures real-time processing and adaptation to new attack patterns, making the system advanced and adaptable.

### Hybrid Detection Model (HDM) Training Phase

The HDM is trained using the AV dataset with a threshold limit. The model combines multiple ML algorithms to enhance the identification of various DDoS attack forms. The resulting hybrid model achieves high accuracy in attack detection.

### Continuous Learning Model (CLM)

The CLM processes the AV dataset and evolved attack patterns in real-time, adapting to new attack patterns dynamically. The model is continuously updated to improve accuracy and adapt to emerging threats.

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

## Results & Discussion

The proposed ADADS achieves a remarkable accuracy of 98.7% with rapid stabilization in a few iterations for the current 6G specifications and applications. The weighted soft voting scheme in the HDM emerged as the optimal choice, surpassing individual algorithms.

## Conclusion & Future Works

ADADS demonstrates resilience and adaptability against evolving DDoS attack patterns in 6G networks. Future works could focus on identifying other types of attack patterns and developing solutions for zero-day vulnerabilities.

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

## Acknowledgement

The authors thank [NGNLab](https://ngnlab.org/), Department of Computer Technology, Anna University, MIT Campus, Chennai 600044, India, for their support.

## Dataset Acknowledgment
   - The dataset used for training and evaluation is the CIC-DDoS2019 dataset.
     ```
     Iman Sharafaldin, Arash Habibi Lashkari, Saqib Hakak, and Ali A. Ghorbani, "Developing Realistic Distributed Denial of Service (DDoS) Attack Dataset and Taxonomy", IEEE 53rd International Carnahan Conference on Security Technology, Chennai, India, 2019.
     ```

