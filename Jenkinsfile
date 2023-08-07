pipeline {
    agent any

    stages {
        stage('Preparation'){
            steps{
                sh 'apt-get update'
                sh  'apt-get install python3.6'
                sh 'python --version'
            }

        }
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python main.py'
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
