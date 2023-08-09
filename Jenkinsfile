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
                sh  '''
                    python -m venv building-env
                    source building-env/bin/activate
                    pip install requests
                    python --version
                    python main.py
                    '''
            }
        }
    }
}
