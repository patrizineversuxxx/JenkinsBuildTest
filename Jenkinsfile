pipeline {
    agent { 
        docker 
        { 
            image 'python:3.11.4-alpine3.18'
        } 
    }
    stages {
        stage('preparation') {
            steps {
                script {
                    def requestsVersion = sh(
                        script: 'python -c "import requests; print(requests.__version__)"',
                        returnStdout: true
                    ).trim()

                    if (requestsVersion) {
                        echo "Python requests module version: ${requestsVersion}"
                    } else {
                        echo "Python requests module not found."
                    }
                }
            }
        }
        stage('build') {
            steps {
                sh  '''
                    python -m venv building-env
                    source building-env/bin/activate
                    if [ -z "$requestsVersion" ]; then
                        pip install requests
                    else
                        pip install --upgrade requests
                    fi
                    python --version
                    python main.py
                    '''
            }
        }
    }
}