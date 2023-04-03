pipeline {
  agent any
  
  parameters {
    choice(
      name: 'RDS_INSTANCE',
      choices: ['database-1', 'database-2', 'database-3'],
      description: 'Select the database instance to snapshot'
    )
  }
// Replace the URL with your GitHub repository URL
  stages {
    stage('Clone Repository') {
      steps {
        git 'https://github.com/asoltes/rds_snapshot.git'

      }
    }
    
    stage('Snapshot') {
      steps {
        python3 rds_snapshot.py -db {param.}
        // Add your build steps here
      }
    }
    
    // Add more stages as needed
  }
}
