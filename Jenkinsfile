pipeline {
    agent any
    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/user/flask-app.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Build and test') {
            steps {
                sh 'python -m pytest'
            }
        }
    }
}
