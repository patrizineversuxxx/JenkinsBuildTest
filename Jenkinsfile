pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                python main.py
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
