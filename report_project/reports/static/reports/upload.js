const csrf  = document.getElementsByName('csrfmiddlewaretoken')[0].value

Dropzone.autoDiscover = false
const myDropzone = new Dropzone('#my-dropozne',{
    url: '/upload/',
    init: function () {
        this.onabort('sending', function(file, xhr, formdata){
            console.log('sending')
            formdata.append('csrfmiddlewaretoken', csrf)
        })

    },
    maxFiles: 3,
    maxFilesize: 3,
    acceptedFiles: '.csv'
})


