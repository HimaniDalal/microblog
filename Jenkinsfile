/*
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'microblog'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'docker run --rm $DOCKER_IMAGE pytest'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    sh 'docker tag $DOCKER_IMAGE username/$DOCKER_IMAGE:latest'
                    sh 'docker push username/$DOCKER_IMAGE:latest'
                }
            }
        }
    }
}
 */

/*
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                sh 'docker build -t microblog-app .'
            }
        }
    }
}
 */
pipeline {
    agent {
        docker {
            image 'python:3.9-slim'  // You can use any Linux-based Docker image here
            label 'microblog_docker'     // Optional, if you have specific agents
        }
    }

   /*  environment {
        // Define any necessary environment variables here
    } */
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/HimaniDalal/microblog.git'
            }
        }
        stage('Build') {
            steps {
               echo "Building..."  // Any shell command that requires Linux-like environment
            }
        }

    }
}
