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
                // Create and activate virtual environment
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests using pytest
                sh 'source venv/bin/activate && pytest --junitxml=test-results.xml'
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
        failure {
            // Notify team of failure
            echo 'Pipeline failed!'
        }
        success {
            echo 'Pipeline succeeded!'
        }
    }
}