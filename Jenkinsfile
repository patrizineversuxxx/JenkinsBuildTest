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
                    def requestsVersion
                    try {
                        requestsVersion = sh(
                            script: 'python -c "import requests; print(requests.__version__)"',
                            returnStdout: true
                        ).trim()
                    } catch (Exception e) {
                        echo "Python requests module not found."
                    }

                    if (requestsVersion) {
                        echo "Python requests module version: ${requestsVersion}"
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
