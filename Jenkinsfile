pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'microblog'
        SONARQUBE_SERVER = 'SonarQube' // Replace with your SonarQube configuration name in Jenkins
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
            }
        }

        stage('SonarQube Scan') {
            steps {
                echo 'Running SonarQube Analysis...'
            }
        }

        stage('Deploy') {
            steps {
               echo 'Running Deployment Stage...'
            }
        }

        stage('Integration Tests') {
            steps {
                echo 'Performing Integration Tests...'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
