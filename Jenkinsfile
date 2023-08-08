pipeline {
    agent {
        label 'jenkins-agent'
    }
    stages {
        stage('preparation') {
            steps {
                sh 'apt-get update'                
                sh 'apt-get install python3.6'
                sh "python --version"
            }
        }
        stage('build') {
            steps {
                echo "Nice job!"
            }
        }
    }
}
