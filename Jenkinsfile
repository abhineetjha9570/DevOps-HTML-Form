pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Files') {
            steps {
                script {
                    if (!fileExists('index.html')) {
                        error('index.html is missing')
                    }

                    if (!fileExists('test_form.py')) {
                        error('test_form.py is missing')
                    }
                }
            }
        }

        stage('Automated HTML Tests') {
            steps {
                bat 'python -m unittest -v test_form.py'
            }
        }
    }

    post {
        always {
            echo 'HTML Form Pipeline execution completed.'
        }

        success {
            echo 'All HTML form tests passed.'
        }

        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}