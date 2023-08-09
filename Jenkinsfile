pipeline {
    agent { 
        docker 
        { 
            image 'python:3.11.4-alpine3.18'
        } 
    }
    stages {
        stage('build') {
            steps {
                sh 'pip install requests'
                sh 'python --version'
                sh 'python main.py'
            }
        }
    }
}
