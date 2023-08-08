pipeline {
    agent {
        label 'jenkins-agent'
    }
    stages {
        stage('preparation') {
            steps {
                sh 'sudo apt-get install python3.6"
                sh 'python --version'
            }
        }
    }
}
