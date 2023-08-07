pipeline {
    agent any

    stages {
        stage('Preparation'){
            steps{
                sh 'sudo apt-get update'
                sh  'sudo apt-get install python3.6'
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
