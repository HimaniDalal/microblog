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
                withSonarQubeEnv(SONARQUBE_SERVER) {
                    bat '''
                        sonar-scanner.bat -Dsonar.projectKey=microblog \
                                          -Dsonar.sources=./ \
                                          -Dsonar.host.url=http://localhost:9000 \
                                          -Dsonar.login=sqa_419b9928563b1cef9e9396d0e23803f99f4b0d7e
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker-compose up -d'
            }
        }

        stage('Integration Tests') {
            steps {
                bat 'python -m unittest discover tests/'
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
