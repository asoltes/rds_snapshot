pipeline {
  agent any
  
    parameters {
        extendedChoice(name: 'RDS_INSTANCE', 
                        description: 'Check the Instance you need to snapshot',
                        type: 'PT_CHECKBOX',
                        value: '',
                        multiSelectDelimiter: ',',
                        groovyScript: """
                            return ['dev', 'qa', 'prod']
                        """
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
        python3 rds_snapshot.py -db $RDS_INSTANCE
        // Add your build steps here
      }
    }
    
    // Add more stages as needed
  }
}
