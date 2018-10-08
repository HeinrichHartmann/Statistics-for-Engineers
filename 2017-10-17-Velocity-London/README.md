# Data Science for Effective Operations @ Velocity London 2017

Event: https://conferences.oreilly.com/velocity/vl-eu/public/schedule/speaker/205186

## Plan

* S1 - Introduction
* S2 - Data Analysis with Python
* S3 - Data Analytics with Graphite and Circonus
* S4 - Math 1 - Descriptive Statistics
* S5 - Math 2 - Comparing Distributions
* S6 - Math 3 - Regressions and Correlation
* S7 - Math 4 - Time Series Analysis
* S8 - Math 5 - Queuing Theory and Universal Scalability

* ./S*.ipynb -- Jupyter Notebooks used in presentation

* /lib/* -- supporting Python libraries

* /datasets/* -- Example datasets and more

The material in this repository is incomplete, in so far as parts of the material were presented on the whiteboard.
So no digital artifacts are available for that.

## Getting Started

1. Setup Strigo
   - Log into this Strigo event: https://app.strigo.io/event/jXg874QKpTCRkoWcX
   - This will give you access to a personal VM in AWS, that we will use in this tutorial.

2. Setup Circonus
   - Create a Circonus account: https://login.circonus.com/signup
   - And provision the strigo VM with a monitoring agent

3. Setup Python Stack:
   - Install docker
     ```
     curl http://get.docker.com/  | sudo bash
     ```
   - Pull this repository from github
     ```
     git clone https://github.com/HeinrichHartmann/DataScience4Ops
     ```
   - Read through Dockerfile and docker.sh
   - Bootstrap work environment:
     ```
     sudo ./docker.sh --create
     ```
   - Run work environment: `suod ./docker.sh --run`
