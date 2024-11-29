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
                // Example: Build Docker Image (Optional)
                bat 'docker build -t %DOCKER_IMAGE% .'
            }
        }

        stage('SonarQube Scan') {
            steps {
                echo 'Running SonarQube Analysis...'
                // Example: Run SonarQube Scanner
                bat '''
                sonar-scanner.bat ^
                    -Dsonar.projectKey=microblog ^
                    -Dsonar.sources=. ^
                    -Dsonar.host.url=http://localhost:9000 ^
                    -Dsonar.login=your-sonarqube-token
                '''
            }
        }

        stage('Deploy') {
            steps {
               echo 'Running Deployment Stage...'
               // Example: Deploy Docker Container
               bat 'docker-compose up -d'
            }
        }

        stage('Integration Tests') {
            steps {
                echo 'Performing Integration Tests...'
                // Install dependencies
                bat 'pip install -r requirements.txt'

                // Run tests
                bat 'pytest microblog_tests/tests --junitxml=report.xml'

                // Archive test results
                junit 'report.xml'
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
