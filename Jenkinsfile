pipeline {
  agent any
  
  parameters {
    extendedChoice(name: 'RDS_INSTANCE', 
                    description: 'Check the Instance you need to snapshot',
                    type: 'PT_CHECKBOX',
                    value: '',
                    multiSelectDelimiter: ',',
                    groovyScript: """
                      return ['database-1', 'database-2', 'database-3', 'database-4']
                    """
    )
  }

  stages {
    stage('Clone Repository') {
      steps {
        git url: 'https://github.com/asoltes/rds_snapshot.git'
      }
    }
    
    stage('Snapshot') {
      steps {
        sh "python3 rds_snapshot.py -db $RDS_INSTANCE"
        // Add your build steps here
      }
    }
    
    // Add more stages as needed
  }
}
