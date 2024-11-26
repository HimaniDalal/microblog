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
