
$(document).ready(function(){
    const submitButton = document.getElementById('submit')
    var dropzone = new Dropzone('#kt_dropzone_file', {
        url: "/api/eixos/import_csv/",
        paramName: "file",
        maxFiles: 10,
        method: 'POST',
        headers: {
            'X-CSRFToken': submitButton.getAttribute('data-csrf'),
        },
        acceptedFiles: "application/csv,text/csv",
        maxFilesize: 10, // MB
        addRemoveLinks: true,
        success: function(params) {
            return toastr.success('Importação iniciado com sucesso!')
        },
        error: function (params) {
            return toastr.error('Erro ao iniciar a importação!')
        }
    })
})
