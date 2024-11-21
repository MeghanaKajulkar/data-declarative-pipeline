pipeline {
    agent any  // Can run on any available agent

    environment {
        PYTHON = 'python'  // Python command on Windows
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone the Git repository
                git 'https://github.com/MeghanaKajulkar/data-declarative-pipeline.git'
            }
        }

        stage('Set up Virtual Environment') {
            steps {
                // Set up virtual environment
                bat '''call setup_venv.bat'''
            }
        }

        stage('Activate Virtual Environment') {
            steps {
                // Activate virtual environment and run the Python script
                bat '''call activate_venv.bat && python clean_data.py'''
            }
        }

        stage('Archive Cleaned Data') {
            steps {
                // Archive the cleaned data files as artifacts
                archiveArtifacts artifacts: 'output/*.csv', allowEmptyArchive: true
            }
        }
    }

    post {
        success {
            // If the pipeline was successful
            echo 'Data cleaning completed successfully!'
        }
        failure {
            // If the pipeline failed
            echo 'Data cleaning failed. Please check the logs.'
        }
    }
}
