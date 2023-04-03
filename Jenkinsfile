pipeline {
  agent any
  
parameters {
        extendedChoice(name: 'rds', 
                       type: 'PT_CHECKBOX', 
                       description: 'Select your database instance',
                       multiSelectDelimiter: ',',
                       quoteValue: false,
                       valueSeparator: ',',
                       visibleItemCount: 3,
                       defaultValue: 'apple,orange',
                       groovyScript: '''
                            return ["database-1", "database-2", "database-3", "database-4", "database-5"]
                        '''
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
        python3 rds_snapshot.py -db {name.choices}
        // Add your build steps here
      }
    }
    
    // Add more stages as needed
  }
}
