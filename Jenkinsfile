pipeline {
    agent any

    stages {
        stage('Preparation'){
            bat 'python --version'
        }
        stage('Build') {
            steps {
                echo 'Building..'
                bat 'python main.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
