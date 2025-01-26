pipeline {
    agent any

    environment {
        // Set Python version (optional)
        PYTHON = 'python3'
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull code from GitHub
                git credentialsId: '74a0b522-6290-43be-9af8-554fac6ca19c', url: 'https://github.com/malakehab2003/alx-backend-python.git', branch: 'master'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests using pytest
                sh 'pytest --junitxml=test-results.xml'
            }
            post {
                always {
                    // Publish test results
                    junit 'test-results.xml'
                }
            }
        }
    }

    post {
        always {
            // Clean up workspace
            cleanWs()
        }
    }
}