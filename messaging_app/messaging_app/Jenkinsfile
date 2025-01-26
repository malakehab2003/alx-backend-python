pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the specified Git branch
                git branch: 'master',
                    credentialsId: '74a0b522-6290-43be-9af8-554fac6ca19c', 
                    url: 'https://github.com/malakehab2003/alx-backend-python.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Create a Python virtual environment
                sh 'python3 -m venv venv'
                // Activate the virtual environment and install dependencies from requirements.txt
                sh 'source venv/bin/activate && pip3 install -r messaging_app/requirements.txt'
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
            // Clean up the workspace
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