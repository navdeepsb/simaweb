###
# @desc
# The Gruntfile to automate all the tasks on client-side.
#
# @author Navdeep
###

module.exports = ( grunt ) ->

    # Load all the plugins:
    grunt.loadNpmTasks "grunt-contrib-sass"
    grunt.loadNpmTasks "grunt-contrib-watch"

    # Config storing directory paths:
    dirConfig =
        styles:
            src: "styles"
            dest: "public/css"
        scripts:
            src: "public/js"
        views:
            index: "templates/_layout.html"

    # Intialize the tasks to perform accordingly:
    grunt.initConfig

        # Get the directory config inside this closure:
        dir: dirConfig

        # Sass @task
        sass:
            options:
                style: "expanded"
            main:
                files:
                    "<%= dir.styles.dest %>/main.css": "<%= dir.styles.src %>/index.scss"

        # Watch @task
        watch:
            files: [ "<%= dir.styles.src %>/*.scss" ]
            tasks: [ "sass" ]

    # Register tasks:
    grunt.registerTask "default", "The default task", [
        "dev"
    ]

    grunt.registerTask "watchify", "Watch files and execute tasks", [
        "sass:main"
        "watch"
    ]

    grunt.registerTask "dev", "Cooks up the front end assets for development", [
        "sass:main"
    ]