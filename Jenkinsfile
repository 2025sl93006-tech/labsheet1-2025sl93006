pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/2025sl93006-tech/labsheet1-2025sl93006.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo Build Stage'
            }
        }

        stage('Test') {
            steps {
                sh '''
                python3 calculator.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
        scp -o StrictHostKeyChecking=no -i /var/lib/jenkins/key.pem calculator.py ec2-user@ec2-51-20-51-77.eu-north-1.compute.amazonaws.com:/home/ec2-user
        '''
            }
        }
    }
}
