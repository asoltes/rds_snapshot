pipeline {
    agent {
        node {
            label 'docker_aws_boto3'
        }
    }
  
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
    stage('Snapshot') {
      steps {
        sh "python3 rds_snap.py -db $RDS_INSTANCE"
        // Add your build steps here
      }
    }
    
    // Add more stages as needed
  }
}
