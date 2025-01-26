pipeline {
    agent {
        docker {
            image 'python:3' // Use the official Python 3 Docker image
        }
    }
    stages {
        stage('Checkout') {
            steps {
                git credentialsId: '74a0b522-6290-43be-9af8-554fac6ca19c', url: 'https://github.com/malakehab2003/alx-backend-python.git', branch: 'master'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'source venv/bin/activate && pytest --junitxml=test-results.xml'
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
        failure {
            echo 'Pipeline failed!'
        }
        success {
            echo 'Pipeline succeeded!'
        }
    }
}